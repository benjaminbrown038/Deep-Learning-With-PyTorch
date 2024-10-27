
!pip install onnx
!pip install onnxruntime
!pip install onnx2keras

import onnx
import onnxruntime
import torch
from torchvision import models
import numpy as np
import cv2
from onnx2keras import onnx_to_keras



resnet = model.resnet18()
resnet.eval()
ip = torch.randn()
with torch.no_grad():
    op = resnet()

print()

torch.onnx.export()

session = onnxruntime.InferenceSession()
input_name
output_name
result 
print

lenet_onnx = cv2.dnn.readNetFromONNX()
lenet_onnx.setInput()
onnx_op = lenet_onnx.forward()

print

onnx_model = onnx.load()
keras_model = onnx_to_keras()
keras_op = keras_model.predict()
print()



