#!/usr/bin/env python3

from setuptools import setup

setup (name = 'jit',
       version = '1.0',
       packages = ['jit'],
       entry_points = {
           'console_scripts' : [
               'jit = jit.cli:main'
           ]
       })
