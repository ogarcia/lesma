#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-2018 Óscar García Amor <ogarcia@connectical.com>
#
# Distributed under terms of the GNU GPLv3 license.

from flask import abort, Blueprint, make_response, request, render_template, send_from_directory, url_for

from pygments import highlight
from pygments.formatters import HtmlFormatter
import pygments.lexers

from tempfile import mkdtemp

import hashlib
import os
import random


PLAIN_TEXT_AGENTS = [
        "curl",
        "httpie",
        "lwp-request",
        "wget",
        "python-requests"
        ]
STORE = os.environ.get('LESMA_STORE', None)

if STORE is None:
    # If store is None then create temp directory
    STORE = mkdtemp()
else:
    if not os.path.exists(STORE):
        # If store non exists, make store path
        try:
            os.makedirs(STORE)
        except Exception as e:
            err = 'Cannot create lesma store directory.\n{0}'.format(e)
            raise SystemExit(err)

# Create sample lesma
sample_lesma_hash = '45392f0c2c5d5b771d61f80e9b4af46a83a6181bb112cc36b439e07c2734bae3'
sample_lesma_path = os.path.join(STORE, sample_lesma_hash)
if not os.path.exists(sample_lesma_path):
    from shutil import copyfile
    copyfile (os.path.realpath(__file__), sample_lesma_path)


def new_id(N=4):
    """
    Returns a pseudo ramdom string with pattern consonant-vowel

    :param N: length consonant-vowel string
    :return: pseudo ramdom string
    :rtype: string
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    odd = ''.join(random.choice(consonants) for _ in range(N))
    even = ''.join(random.choice(vowels) for _ in range(N))
    nid = ''.join(odd[n] + even[n] for n in range(N))
    return nid


def new_hash(N=4):
    """
    Returns a tuple with a pseudo ramdom string with pattern consonant-vowel and
    its sha256 hash

    :param N: length consonant-vowel string
    :return: tuple(pseudo ramdom string, sha256 hash)
    :rtype: tuple
    """
    nid = new_id(N)
    nhash = hashlib.sha256(nid.encode()).hexdigest()
    while os.path.isfile(os.path.join(STORE, nhash)):
        nid = nid(N)
        nhash = hashlib.sha256(nid.encode()).hexdigest()
        N += 1
    return (nid, nhash)


def read(id):
    """
    Read file from store

    :param id: id of file
    :return: binary file contents or None if not found
    :rtype: binary or None
    """
    id_hash = hashlib.sha256(id.encode()).hexdigest()
    if os.path.isfile(os.path.join(STORE, id_hash)):
        with open(os.path.join(STORE, id_hash), 'rb') as f:
            lesma = f.read()
        return lesma
    return None


def write(id_hash, data):
    """
    Write file to store

    :param id_hash: a tuple from new_hash()
    :param data: file contents
    :return: file id
    :rtype: string
    """
    id, hash = id_hash
    with open(os.path.join(STORE, hash), 'w') as f:
        f.write(data)
    return id


lesma = Blueprint('lesma', __name__)


@lesma.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lesma = request.form['lesma']
        if lesma == '':
            # Prevents the creation of empty lesmas
            redirect = url_for('.index', _external=True)
        else:
            nid = write(new_hash(), lesma)
            redirect = url_for('.get_lesma', lesma_id=nid, _external=True)
        response = make_response('{}\n'.format(redirect), 303)
        response.headers['Location'] = redirect
        return response
    user_agent = request.headers.get('User-Agent', '').lower()
    if any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
        return get_help()
    return render_template('index.html', editable=True)


@lesma.route('/<lesma_id>')
def get_lesma(lesma_id):
    user_agent = request.headers.get('User-Agent', '').lower()
    lesma_name, lesma_format = os.path.splitext(lesma_id)
    lesma_content = read(lesma_name)
    if lesma_content is not None:
        raw = request.args.get('raw')
        if raw is not None or any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
            return make_response(lesma_content, {'Content-Type': 'text/plain; charset=UTF-8'})
        try:
            lesma_lexer = pygments.lexers.get_lexer_by_name(lesma_format[1:] if len(lesma_format) > 1 else 'txt')
        except Exception:
            lesma_lexer = pygments.lexers.TextLexer()
        return render_template('lesma.html', lesma_id=lesma_id, lesma=highlight(lesma_content, lesma_lexer, HtmlFormatter(lineanchors='n', linenos='table')))
    if any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
        return ('lesma not found\n', 404)
    return (render_template('404.html', error="lesma not found"), 404)


@lesma.route('/clone/<lesma_id>')
def clone_lesma(lesma_id):
    lesma_name, lesma_format = os.path.splitext(lesma_id)
    lesma_content = read(lesma_name)
    if lesma_content is not None:
        return render_template('index.html', editable=True, lesma=lesma_content.decode('utf-8'))
    return (render_template('404.html', error="lesma not found"), 404)


@lesma.route('/:help')
def get_help():
    user_agent = request.headers.get('User-Agent', '').lower()
    raw = request.args.get('raw')
    if raw is not None or any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
        return make_response(render_template('help.txt'), {'Content-Type': 'text/plain; charset=UTF-8'})
    return render_template('help.html', help=True)


# Serve favicon
@lesma.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(lesma.root_path, 'static', 'img'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
