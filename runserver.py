#!/usr/bin/env python
# -*- coding: utf-8 -*-

from project import app
from project.models import fensi
from project.controller import printer

if __name__=='__main__':
    app.run('0.0.0.0', port=9000, debug=True)
