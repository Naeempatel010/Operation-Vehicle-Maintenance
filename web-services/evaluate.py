
import os
import cv2
import sys
import random
import math
import re
import time
import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import skimage
import glob

# Root directory of the project
ROOT_DIR = os.getcwd()

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

import custom 

#%matplotlib inline 

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

custom_WEIGHTS_PATH = "mask_rcnn_damage_0010.h5"  # TODO: update this path

config = custom.CustomConfig()
custom_DIR = os.path.join(ROOT_DIR, "customImages")

class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

# Device to load the neural network on.
# Useful if you're training a model on the same 
# machine, in which case use CPU and leave the
# GPU for training.
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0

# Inspect the model in training or inference modes
# values: 'inference' or 'training'
# TODO: code for 'training' test mode not ready yet
TEST_MODE = "inference"

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

#dataset = custom.CustomDataset()
#dataset.load_custom(custom_DIR, "val")

# Must call before using the dataset
#dataset.prepare()

#print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))


with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR,
                              config=config)

# load the last model you trained
# weights_path = model.find_last()[1]

# Load weights
print("Loading weights ", custom_WEIGHTS_PATH)
model.load_weights(custom_WEIGHTS_PATH, by_name=True)



from importlib import reload # was constantly changin the visualization, so I decided to reload it instead of notebook
reload(visualize)

"""
image_id = random.choice(dataset.image_ids)
image, image_meta, gt_class_id, gt_bbox, gt_mask =\
    modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
info = dataset.image_info[image_id]
print("image ID: {}.{} ({}) {}".format(info["source"], info["id"], image_id, 
                                       dataset.image_reference(image_id)))
"""
def predict_mask(file):
    path = file

    images = skimage.io.imread(path)

    # Run object detection
    results = model.detect([images], verbose=1)
    class_names=["1","2","3"]
    # Display results
    ax = get_ax(1)
    r = results[0]
    #checkmask(r['rois'])
    #print(type(images))
    visualize.display_instances(images, r['rois'], r['masks'], r['class_ids'], 
                                 class_names, r['scores'], ax=ax,
                                title="Predictions")
#log("gt_class_id", gt_class_id)
#og("gt_bbox", gt_bbox)
#log("gt_mask", gt_mask)
def checkmask(file,destination_file):
    path = file
    new_path = destination_file
    images = skimage.io.imread(path)
    results = model.detect([images], verbose=1)
    class_names=["1","2","3"]
    # Run object detection
    r=results[0]

    N=r['rois'].shape[0]
    if not N:
        return 0

    else:
        ax=get_ax()
        visualize.display_instances(images,r['rois'],r['masks'],r['class_ids'],class_names,r["scores"],ax=ax,title="",filename=new_path)
        return 1






