import base64


def encode_b64(input_str):
    enc_str = base64.b64encode(input_str.encode("UTF-8")).decode("UTF-8")
    print(f"Encoded str->{enc_str}")
    return enc_str
