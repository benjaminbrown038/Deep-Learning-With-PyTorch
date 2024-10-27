import torch
import torchvision
import collections 
from torchvision.models.detection import faster_rcnn, rpn, image_list, FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator
import torchvision.models as models
from torchvision.ops import MultiScaleRoIAlign


alexnet = models.alexnet(pretrained = False)
print(alexnet)

backbone = alexnet.features

image
backbone_op
print

rpn_layer 

object_score, bbox_locs 
print

anchor_generator

rpn_pre_nms
rpn_post_nms
region_proposer

print

inputs
rpn_bbox

print

num_boxes

fixed_size_pooler = 
inp1
inp2
inp3
out1
out2
out3

print

roi_pooler

fmaps
rpn_bbox_rand
roi_pooling_op

mlp_head
print
mlp_op
print

final_layer 







