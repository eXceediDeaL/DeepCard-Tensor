import torch
from torch.autograd import Variable
import utils
import mydataset
from PIL import Image
import numpy as np
import crnn_ex as crnn
import cv2
import torch.nn.functional as F
import keys

gpu = True
if not torch.cuda.is_available():
    gpu = False

model_path = './crnn_models/CRNN_0406_sim_76_890.pth'
alphabet = keys.alphabet
imgH = 32
imgW = 440
model = crnn.CRNN(imgH, 1, len(alphabet) + 1, 256)
if gpu:
    model = model.cuda()
print('loading pretrained model from %s' % model_path)
if gpu:
    model.load_state_dict( torch.load( model_path ) )
else:
    model.load_state_dict(torch.load(model_path,map_location=lambda storage,loc:storage))
print('done')
print('starting...')
converter = utils.strLabelConverter(alphabet)
transformer = mydataset.resizeNormalize3((imgW, imgH))

def recognize_downline(img,crnn_model=model):
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    image = Image.fromarray(np.uint8(img)).convert('L')
    image = transformer( image )
    if gpu:
        image = image.cuda()
    # image = image.view( 1, *image.size() )


    model.eval()
    preds = model( image )

    preds = F.log_softmax(preds,2)
    conf, preds = preds.max( 2 )
    preds = preds.transpose( 1, 0 ).contiguous().view( -1 )

    preds_size = Variable( torch.IntTensor( [preds.size( 0 )] ) )
    raw_pred = converter.decode( preds.data, preds_size.data, raw=True )
    sim_pred = converter.decode( preds.data, preds_size.data, raw=False )
    return sim_pred.upper()

def recognize_PIL_image(img):
    image = transformer(img)
    if gpu:
        image = image.cuda()
    # image = image.view(1, *image.size())
    # image = Variable(image)

    model.eval()
    preds = model(image)

    preds = F.log_softmax(preds, 2)
    conf, preds = preds.max(2)
    preds = preds.transpose(1, 0).contiguous().view(-1)

    preds_size = Variable(torch.IntTensor([preds.size(0)]))
    raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
    sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
    return sim_pred.upper()

if __name__ == '__main__':
    fname = 'data/images/000059.jpg'
    img = cv2.imread(fname)
    res = recognize_downline(img)
    print(res)





