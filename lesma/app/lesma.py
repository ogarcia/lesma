#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Óscar García Amor <ogarcia@connectical.com>
#
# Distributed under terms of the GNU GPLv3 license.

import bottle

from pygments import highlight
from pygments.formatters import HtmlFormatter
import pygments.lexers

try:
    from urlparse import urljoin
except ModuleNotFoundError:
    from urllib.parse import urljoin

from pkg_resources import resource_filename
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
store = os.environ.get('LESMA_STORE', None)

if store is None:
    # If store is None then create temp directory
    store = mkdtemp()
else:
    if not os.path.exists(store):
        # If store non exists, make store path
        try:
            os.makedirs(store)
        except Exception as e:
            err = 'Cannot create lesma store directory.\n{0}'.format(e)
            raise SystemExit(err)
# Create sample lesma
sample_lesma_hash = '45392f0c2c5d5b771d61f80e9b4af46a83a6181bb112cc36b439e07c2734bae3'
sample_lesma_path = os.path.join(store, sample_lesma_hash)
if not os.path.exists(sample_lesma_path):
    from shutil import copyfile
    copyfile (resource_filename(__name__, 'lesma.py'), sample_lesma_path)


def new_id(N=4):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    odd = ''.join(random.choice(consonants) for _ in range(N))
    even = ''.join(random.choice(vowels) for _ in range(N))
    nid = ''.join(odd[n] + even[n] for n in range(N))
    return nid


def new_hash(N=4):
    nid = new_id(N)
    nhash = hashlib.sha256(nid.encode()).hexdigest()
    while os.path.isfile(os.path.join(store, nhash)):
        nid = nid(N)
        nhash = hashlib.sha256(nid.encode()).hexdigest()
        N += 1
    return (nid, nhash)


def read(id):
    id_hash = hashlib.sha256(id.encode()).hexdigest()
    if os.path.isfile(os.path.join(store, id_hash)):
        with open(os.path.join(store, id_hash), 'rb') as f:
            lesma = f.read()
        return lesma
    return None


def write(id_hash, data):
    id, hash = id_hash
    with open(os.path.join(store, hash), 'w') as f:
        f.write(data)
    return id


# Set template and static files location
bottle.TEMPLATE_PATH.insert(0, resource_filename(__name__, 'templates'))
static_path = resource_filename(__name__, 'static')


@bottle.get('/')
def get():
    return bottle.template('index', lesma='')


@bottle.post('/')
def post():
    lesma = bottle.request.forms.get('lesma')
    if lesma:
        nid = write(new_hash(), lesma)
        redirect = urljoin(bottle.request.url, nid)
        bottle.response.status = 303
        bottle.response.set_header('Location', redirect)
        return '{}\n'.format(redirect)
    else:
        bottle.abort(400, "No data received")


@bottle.get('/<lesma_id>')
def get_lesma(lesma_id):
    lesma_name, lesma_format = os.path.splitext(lesma_id)
    lesma_content = read(lesma_name)
    if lesma_content is not None:
        raw = bottle.request.query.get('raw')
        user_agent = bottle.request.headers.get('User-Agent').lower()
        if raw is not None or any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
            bottle.response.content_type = 'text/plain; charset=UTF-8'
            return lesma_content
        try:
            lesma_lexer = pygments.lexers.get_lexer_by_name(lesma_format[1:] if len(lesma_format) > 1 else 'txt')
        except Exception:
            lesma_lexer = pygments.lexers.TextLexer()
        return bottle.template('lesma', lesma_id=lesma_id, lesma=highlight(lesma_content, lesma_lexer, HtmlFormatter(lineanchors='n', linenos='table')))
    bottle.abort(404, "No lesma found")


@bottle.get('/clone/<lesma_id>')
def clone_lesma(lesma_id):
    lesma_name, lesma_format = os.path.splitext(lesma_id)
    lesma_content = read(lesma_name)
    if lesma_content is not None:
        return bottle.template('index', lesma=lesma_content)
    bottle.abort(404, "No lesma found")


@bottle.get('/\:help')
def get_help():
    user_agent = bottle.request.headers.get('User-Agent').lower()
    if any(agent in user_agent for agent in PLAIN_TEXT_AGENTS):
        bottle.response.content_type = 'text/plain; charset=UTF-8'
        with open(os.path.join(static_path, 'help', 'help.txt'), 'r') as f:
            help = f.read()
        return help
    return bottle.template('help', lesma_id=':help')


# Serve static content
@bottle.get('/favicon.ico')
def get_favicon():
    return bottle.static_file('favicon.ico', root=os.path.join(static_path, 'img'))


@bottle.get('/css/<file>')
def get_css(file):
    return bottle.static_file(file, root=os.path.join(static_path, 'css'))


@bottle.get('/img/<file>')
def get_img(file):
    return bottle.static_file(file, root=os.path.join(static_path, 'img'))


@bottle.get('/js/<file>')
def get_js(file):
    return bottle.static_file(file, root=os.path.join(static_path, 'js'))
