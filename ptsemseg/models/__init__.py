#Adapted from https://github.com/meetshah1995/pytorch-semseg/tree/master/ptsemseg
import torchvision.models as models

from ptsemseg.models.fcn import *
"""
from ptsemseg.models.segnet import *


"""
def get_model(name, n_classes, version=None):
    #model = _get_model_instance(name)
    model= fcn8s
    print(name)

    if name in ['frrnA', 'frrnB']:
        model = model(n_classes, model_type=name[-1])

    elif name in ['fcn32s', 'fcn16s', 'fcn8s']:
        print(model)
        #model = model(n_classes=n_classes)
        #vgg16 = models.vgg16(pretrained=True)
        #model.init_vgg16_params(vgg16)

    elif name == 'segnet':
        model = model(n_classes=n_classes,
                      is_unpooling=True)
        vgg16 = models.vgg16(pretrained=True)
        model.init_vgg16_params(vgg16)

    elif name == 'unet':
        model = model(n_classes=n_classes,
                      is_batchnorm=True,
                      in_channels=3,
                      is_deconv=True)

    elif name == 'pspnet':
        model = model(n_classes=n_classes, version=version)

    elif name == 'icnet':
        model = model(n_classes=n_classes, with_bn=False, version=version)
    elif name == 'icnetBN':
        model = model(n_classes=n_classes, with_bn=True, version=version)

    else:
        model = model(n_classes=n_classes)

    return model

def _get_model_instance(name):
    try:
        return {
            'fcn32s': fcn32s,
            'fcn8s': fcn8s,
            'fcn16s': fcn16s,
            'unet': unet,
            'segnet': segnet,
            'pspnet': pspnet,
			'icnet': icnet,
			'icnetBN': icnet,
            'linknet': linknet,
            'frrnA': frrn,
            'frrnB': frrn,
        }[name]
    except:
        print('Model {} not available'.format(name))
