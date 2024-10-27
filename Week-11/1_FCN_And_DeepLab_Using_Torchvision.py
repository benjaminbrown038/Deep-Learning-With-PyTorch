%matplotlib inline
from torchvision import models
import torch
import torchvision.transforms as T

from PIL import Image

import matplotlib.pyplot as plt
import urllib
import numpy as np
import time



fcn_resnet101 = model.segmentations.fcn_reset101(pretrained=True).eval()
deeplabv3_resnet101 = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()



