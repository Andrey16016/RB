import base64, functools; exec(functools.reduce(lambda current_bytes, _: base64.b64decode(current_bytes), range(2), open('local', "r", encoding='utf-8').read().encode('utf-8')).decode('utf-8'))
