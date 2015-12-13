import inspect
import os
import sys

__file__ = os.path.abspath(inspect.getsourcefile(lambda _: None))
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from challenge1 import hex_to_base64


def test_hex_to_base64():
    hex_string = '49276d206b696c6c696e6720796f7572206272' \
                 '61696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    base64_string = hex_to_base64(hex_string)
    assert base64_string == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBs' \
                            b'aWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
