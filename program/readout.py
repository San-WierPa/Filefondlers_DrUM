# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:35:15 2020

@author: SePa
"""

# depth readout

import matplotlib.pyplot as plt
import numpy as np
import datetime
from glob import glob

depths_files="slow_control/depth_*txt"
depths_f=sorted(glob(depths_files))
#print(depths_f)

dtime=[]
depth=[]

for df in depths_f:
    print(df)
    f=open(df)
    i=0
    for line in f:
        words=line.replace("\n", "").split(" ")
        try:
            d=words[-1]
            d=float(d)
            d=-d
            t=words[0]
            t=str(t)
            t1=datetime.datetime.strptime(t, "%Y%m%d_%H_%M_%S").timestamp()
            t1=int(t1)
            
            
            # correct false depth readout due to lacking software
            if df=="slow_control/depth_20191214_00_05_15.txt" or \
               df=="slow_control/depth_20191214_00_22_41.txt" or \
               df=="slow_control/depth_20191214_07_32_08.txt":
                d=d*2.08
        
            # correct wrong zero depth
            if len(dtime)>0:
                if d>=-250:
                    rt=t1-dtime[0]
                    rt=rt/(60*60)
                    if rt>2.5 and rt<14.5:
                        continue
                if d>=-1000:
                    rt=t1-dtime[0]
                    rt=rt/(60*60)
                    if rt>10 and rt<12:
                        continue
                
        
            dtime.append(t1)
            depth.append(d)
        except Exception as e:
            print(e)        
        i+=1
        #if i<10: print(d)
    f.close()
#print(depth)
print(type(dtime),dtime[:10])
depth=np.array(depth)
dtime=np.array(dtime)