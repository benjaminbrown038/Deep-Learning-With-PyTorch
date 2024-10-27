!git clone https://github.com/facebookresearch/detectron2.git

%cd detectron2/projects/DensePose

import urllib 
import cv2
import numpy as np
from typing import ClassVar, Dict
from detectron2.config import get_cfg
from detectron2.structures.instances import Instances
from detectron2.engine.defaults import DefaultPredictor

from denspose import add_denspose_config
from densepose.vis.base import CompoundVisualizer
from densepose.vis.bounding_box import ScoreBoundingBoxVisualizer
from densepose.vis.extractor import CompoundExtractor, create_extractor

from denspose.vis.denspose_results import DensePoseResultsContourVisualizer,
                                          DensePoseResultsFineSegmentationVisualizer,
                                          DensePoseResultsUVisualizer,
                                          DensePoseResultsVVisualizer

def download():


VISUALIZERS: ClassVar[Dict[str, object]] = {
    "dp_contour": DensePoseResultsContourVisualizer,
    "dp_segm": DensePoseResultsFineSegmentationVisualizer,
    "dp_u": DensePoseResultsUVisualizer,
    "dp_v": DensePoseResultsVVisualizer,
    "bbox": ScoredBoundingBoxVisualizer,
}

def setConfig():
    return cfg

def getVisAndExtract():
    return extractor, visualizer

def createContext():
    return context

def predict():
    return image_vis

def inferenceOnVideo():
    

