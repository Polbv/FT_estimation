import os
import cv2
import torch.nn as nn
import torchvision
import pathlib
import numpy as np


torchvision.

path='./videos/in'
samples=os.listdir(path)
N=len(samples)
for i in samples:
    video=cv2.videoCapture(i)
    
