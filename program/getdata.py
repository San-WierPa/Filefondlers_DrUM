# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:33:22 2020

@author: SePa
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
from glob import glob

# get manual depth data
surf_log_files="surface/log/*log"
log_f=sorted(glob(surf_log_files))
#print(log_f)

ltime=[]
ldepth=[]
i=0
for lf in log_f:
    print(lf)
    f=open(lf)
    
    for line in f:
        if "LMSG" in line:
            words=line.replace("\n", "").split("LMSG:")
            msg=words[-1]
            #print(msg)
            if msg[0]=="T" or "Estisol" in msg: 
                continue 
            d=msg.replace("D ", "").replace("D", "").replace("at", "").replace(" m", "")
            try:
                d=float(d)
                t=line.split(":")[0]
                t1=datetime.datetime.strptime(t, "%Y%m%d_%H_%M_%S").timestamp()
                print(t1)
                print(d)
                ltime.append(t1)
                ldepth.append(-d)
            except:
                pass
            
            i+=1
        #if i>10: break
    #if i>10: break
        
    f.close()
ldepth=np.array(ldepth)
ltime=np.array(ltime)