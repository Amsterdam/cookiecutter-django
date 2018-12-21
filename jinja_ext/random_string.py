# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from jinja2 import nodes
from jinja2.ext import Extension

import random
import string

from cookiecutter.main import cookiecutter

def pw_gen(chars=string.ascii_letters + string.digits + '#$%&()*+,-.;<=>?[]_{|}~'):
    size = random.randint(16,30)
    return ''.join(random.choice(chars) for _ in range(size))

def random_string(value):
    generated = pw_gen()
    return generated.replace("'", "$")  # prevent headaches in bash

class RandomExtension(Extension):
    def __init__(self, environment):
        super(RandomExtension, self).__init__(environment)
        environment.filters['random_string'] = random_string
