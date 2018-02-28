#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-2018 Óscar García Amor <ogarcia@connectical.com>
#
# Distributed under terms of the GNU GPLv3 license.

import os
import sys

from lesma.app import app


DEFAULT_DEVEL_HOST = '127.0.0.1'
DEFAULT_DEVEL_PORT = 7766
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 7777


def dev():
    """dev [host] [port]
    Run a development server in specific host and port.
    Aditionally you can specify the following environment variables.
    - LESMA_HOST, the hostname to listen on.
    - LESMA_PORT, the port of the webserver.
    - LESMA_STORE, the path for store lesmas.

    Never use this server for production.
    """
    host = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('LESMA_HOST', DEFAULT_DEVEL_HOST)
    port = int(sys.argv[3]) if len(sys.argv) > 3 else int(os.environ.get('LESMA_PORT', DEFAULT_DEVEL_PORT))

    app.run(host=host, port=port, debug=True)


def server():
    """server [host] [port]
    Run a production server in specific host and port.
    Aditionally you can specify the following environment variables.
    - LESMA_HOST, the hostname to listen on.
    - LESMA_PORT, the port of the webserver.
    - LESMA_STORE, the path for store lesmas.
    """
    host = sys.argv[2] if len(sys.argv) > 2 else None
    port = int(sys.argv[3]) if len(sys.argv) > 3 else None
    wsgi(host, port)


def wsgi(host=None, port=None):
    """Return WSGI server for application"""
    host = os.environ.get('LESMA_HOST', DEFAULT_HOST) if host is None else host
    port = int(os.environ.get('LESMA_PORT', DEFAULT_PORT)) if port is None else port

    from gevent.pywsgi import WSGIServer
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    print('Serving on http://{}:{}/'.format(host, port))
    WSGIServer((host, port), app).serve_forever()


def cli():
    """Command line script."""
    if len(sys.argv) > 1:
        if sys.argv[1] == 'cli':
            print('Nope')
        else:
            try:
                return globals()[sys.argv[1]]()
            except KeyError:
                print('{} is not a valid argument'.format(sys.argv[1]))
    else:
        for x, y in globals().items():
            if x != 'app' and x != 'cli' and x != 'wsgi' and x[0] != '_' and hasattr(y, '__call__') and hasattr(y, '__doc__'):
                print('%s' % (y.__doc__,))
