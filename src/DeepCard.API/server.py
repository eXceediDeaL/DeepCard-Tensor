from wsgiref.simple_server import make_server
import traceback
import base64
from io import BytesIO
from PIL import Image
import json

def base64_to_image(base64_str):
    byte_data = base64.b64decode(base64_str)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img

def get_result(img):
    import ocr2 as ocr
    import numpy as np
    image = np.array(img.convert('RGB'))
    result, _ = ocr.model(image)
    res = ""
    for key in result:
        cs = result[key][1]
        if not cs.isdigit():
            continue
        if len(cs) > len(res):
            res = cs
    return res

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    try:
        request_body = environ['wsgi.input'].read(request_body_size)
        # print(request_body)
        img = base64_to_image(request_body)
        res = get_result(img)
    except Exception as e:
        res = "Error"
        print(e)
        traceback.print_exc()

    print("Result:", res)

    start_response('200 OK', [('Content-Type', 'application/json')])
    return [json.dumps(res).encode("utf-8")]

if __name__ == '__main__':
    httpd = make_server('', 4000, application)
    print('Server running...')
    httpd.serve_forever()