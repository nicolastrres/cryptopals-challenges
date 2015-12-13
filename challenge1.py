import binascii
import base64


def hex_to_base64(hex_string):
    binary_data = binascii.unhexlify(hex_string)
    return base64.b64encode(binary_data)
