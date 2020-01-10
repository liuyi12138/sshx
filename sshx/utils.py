import os
import sys
import json
import string
import random

from getpass import getpass

from . import tokenizer
from . import const as c


class ClsDictEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def random_str(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(15)])


def is_str(s):
    return isinstance(s, str)


def json_dump(obj):
    return json.dumps(obj, cls=ClsDictEncoder)


def json_load(s):
    return json.loads(s)


def read_password(prompt='Password:'):
    '''Read password from PTY'''
    return getpass(prompt=prompt)


def read_passphrase():
    return read_password(prompt='Passphrase:')


def parse_user_host_port(s):
    '''
    user@host:port -> (user, host, port)
    '''
    user, host_port = s.split('@')
    splited = host_port.split(':')

    if len(splited) == 2:
        host, port = splited
    else:
        host, port = splited[0], c.DEFAULT_PORT

    return user, host, port
