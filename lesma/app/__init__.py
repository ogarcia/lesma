#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-2018 Óscar García Amor <ogarcia@connectical.com>
#
# Distributed under terms of the GNU GPLv3 license.

from flask import Flask

from .lesma import lesma


app = Flask(__name__)
app.register_blueprint(lesma)
