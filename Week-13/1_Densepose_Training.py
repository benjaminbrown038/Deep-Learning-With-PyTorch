!git clone https://github.com/facebookresearch/detectron2.git

%cd detectron2/projects/DensePose

import urllib
import zipfile

def download():

prepared_data_link 
dataset_zip

def unzip():


!ls datasets/coco/annotations

import logging
import os
from collections import OrderedDict

import detectron2.utils.comm as comm
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import CfgNode, get_cfg
from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultTrainer, default_argument_parser, default_setup, hooks, launch
from detectron2.evaluation import COCOEvaluator, DatasetEvaluators, verify_results
from detectron.models import DatasetMapperTTA 
from detectron.utils.logger import setup_logger
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.utils.visualizer import Visualizer

from densepose import DensePoseCOCOEvaluator, DensePoseGeneralizedRCNNWithTTA, add_dataset_category_config, add_densepose_config, load_from_cfg
from densepose.data import DatasetMapper, build_detection_test_loader, build_detection_train_loader

import cv2 
import matplotlib.pyplot as plt

from attrdict import AttrDict

!python query_db.py show densepose_coco_2014_train image_id:int=785 bbox,dp_i -v

img 
plt
plt
plt

def setup():

class Trainer():
    @classmethod
    def build_evaluator():
    @classmethod
    def build_test_loader():
    @classmethod
    def build_train_loader():
    @classmethod
    def test_with_TTA():


if __name__ == '__main__':
    attr_dict = {}

def main():

