# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:10:38 2018

@author: XZK
"""
# In[1]: Read data 
import json
with open("3615516147724578.json","r") as load_f:
    load_dict = json.load(load_f);

import numpy as np
from math import sqrt

General_Fz = np.array(load_dict["Signals"][0]["Values"])
General_COPx = np.array(load_dict["Signals"][1]["Values"])
General_COPy = np.array(load_dict["Signals"][2]["Values"])

dt=0.001
Length=range(30000-1)
Time=30

# In[2]: Feature extraction
feature = np.zeros(96)

def swayPath(x, y):
    length=0
    for i in Length:
        length += sqrt((x[i+1] - x[i]) * (x[i+1] - x[i]) + (y[i+1] - y[i]) * (y[i+1] - y[i]))
    
    return length


def swayPath1(sig):
    length=0
    for i in Length:
        length += abs(sig[i+1] - sig[i])
    
    return length

# Sway Path
feature[0] = swayPath(General_COPx, General_COPy)
feature[1] = swayPath1(General_COPy)
feature[2] = swayPath1(General_COPx)

# Sway V
feature[3] = feature[0] / Time
feature[4] = feature[1] / Time
feature[5] = feature[2] / Time

# Sway average amplitude
from detect_peaks import detect_peaks

# Sway maximal amplitude
feature[8] = General_COPy.max() - General_COPy.min()
feature[9] = General_COPx.max() - General_COPx.min()
# Sway area

# Sway area per second

# Area of 100% ellipse

# FRE from peaks

# Mean FRE of total spectrum

# Peak FRE of total spectrum

# Mean FRE of 0.1-1 spectrum band

# Mean FRE of 1-2 spectrum band

# Mean FRE of 2-10 spectrum band
