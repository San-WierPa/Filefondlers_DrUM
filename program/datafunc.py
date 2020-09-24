# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:36:59 2020

@author: SePa
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
from glob import glob

def timeToDepth(times):
    # from depth and dtime
    de=[]
    j=0
    # go through new times
    for s in times:
        #print(s)
        j+=1
        d=0
        # search for match
        for i in range(len(dtime)-1):
            if s >= dtime[i] and s<dtime[i+1]:
                
                d=(depth[i+1]+depth[i])/2
                #print("Found for %f: %f %f %f" %(s, depth[i+1], depth[i], d))
                break
        de.append(d)
        #if j>100: break
    return de
mdepth=timeToDepth(mtime)
mdepth=np.array(mdepth)