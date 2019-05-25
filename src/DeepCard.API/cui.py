from wsgiref.simple_server import make_server
import traceback
import base64
from io import BytesIO
from PIL import Image
import json
from glob import glob
import os
import shutil

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

if __name__ == '__main__':
    image_files = glob('./test_images/*.*')
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)

    txt_file = os.path.join(result_dir, 'result.txt')
    txt_f = open(txt_file, 'w')

    for image_file in sorted(image_files):
        if ".gitkeep" in image_files:
            continue
        result = get_result(Image.open(image_file))
        txt_f.write(image_file.split('/')[-1].split('.')[0] + ':' + result + '\n')
    
    txt_f.close()

