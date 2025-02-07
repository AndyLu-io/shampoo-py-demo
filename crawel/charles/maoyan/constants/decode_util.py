def decode_text(text):
    decoded_string = text.encode('utf-8').decode('unicode-escape')
    return decoded_string


text = decode_text("\\u5362\\u6653\\u6CE2")
print(text)
