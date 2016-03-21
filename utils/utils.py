from os import urandom
from base64 import b64encode
import random


def generate_object_id(size=10):
    CHAR_MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '0123456789'
    # rand = urandom(8)
    # print int(rand.encode('hex'), 16)
    # token = b64encode(rand).decode('utf-8')
    return ''.join(random.choice(CHAR_MAP) for _ in range(size))
