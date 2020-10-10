# -*- coding: utf-8 -*-
"""
Created on Sep 28 18:48:36 2020

@author: SePa
"""

from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_diff import delta_e_cie1976
from colormath.color_diff import delta_e_cmc
from colormath.color_diff import delta_e_cie1994

class deltaE():
    def __init__(self, lab_L, lab_a, lab_b, sam_L, sam_a, sam_b):
        self.lab_L = lab_L
        self.lab_a = lab_a
        self.lab_b = lab_b
        self.sam_L = sam_L
        self.sam_a = sam_a
        self.sam_b = sam_b

    def color1(self, lab_L, lab_a, lab_b):
        return LabColor(self.lab_L, self.lab_a, self.lab_b)

    def color2(self, sam_L, sam_a, sam_b):
        return LabColor(self.sam_L, self.sam_a, self.sam_b)

    def DeltaE2000(self):
        reference = self.color1(self.lab_L, self.lab_a, self.lab_b)
        sample = self.color2(self.sam_L, self.sam_a, self.sam_b)
    
        return delta_e_cie2000(reference, sample)
    
    def DeltaE1976(self):
        reference = self.color1(self.lab_L, self.lab_a, self.lab_b)
        sample = self.color2(self.sam_L, self.sam_a, self.sam_b)
        
        return delta_e_cie1976(reference, sample)
    
    def DeltaECMC(self):
        reference = self.color1(self.lab_L, self.lab_a, self.lab_b)
        sample = self.color2(self.sam_L, self.sam_a, self.sam_b)
        
        return delta_e_cmc(reference, sample)
   

### outputs
#measE2000 = deltaE(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#delE2000 = measE2000.DeltaE2000()

#print(delE2000)


#measE1976 = deltaE(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#delE = measE1976.DeltaE1976()

#print(delE)


measEcmc = deltaE(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
delEcmc = measEcmc.DeltaECMC()

print(delEcmc)



    