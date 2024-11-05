from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import _init_paths

import os
from tqdm import tqdm

import cv2
import pycocotools.coco as coco
from opts import opts
from detectors.detector_factory import detector_factory

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'bmp', 'tiff']

def demo(image):
  opt = opts().init()
  os.environ['CUDA_VISIBLE_DEVICES'] = 0
  opt.debug = max(opt.debug, 1)
  Detector = detector_factory[opt.task]
  detector = Detector(opt)
  ret = detector.run(opt, image)
  return ret
if __name__ == "__main__":
	import cv2
	img = cv2.imread('sample/table_1.png')
	demo(img)