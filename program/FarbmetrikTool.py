# -*- coding: utf-8 -*-
"""
Created on Sep 28 18:48:36 2020

@author: SePa
"""

import colour
from colormath.color_objects import LabColor, XYZColor, AdobeRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_diff import delta_e_cie1976
from colormath.color_diff import delta_e_cmc
#from colormath.color_diff import delta_e_cie1994
from colormath.color_objects import BaseRGBColor
#import pip


class FarbmetrikTools1():
    def __init__(self, lab_L, lab_a, lab_b, sam_L, sam_a, sam_b):
        self.lab_L = lab_L
        self.lab_a = lab_a
        self.lab_b = lab_b
        self.sam_L = sam_L
        self.sam_a = sam_a
        self.sam_b = sam_b

    def color1(self):
        return LabColor(self.lab_L, self.lab_a, self.lab_b)

    def color2(self):
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
    
    def colorimetry(self):
        colorimetryConversion = colour.colorimetry
        return colorimetryConversion
    
    ### Hunter L,a,b Colour Scale - Python: Colour 5.4.12.6
    def cie_hue(self):
        XYZ = [self.sam_L, self.sam_a, self.sam_b]
        return colour.XYZ_to_Hunter_Lab(XYZ)
    
    ### with given spectral distribution, following method can compute chromacity coordinates
    def cie_chrome(self):
        XYZ = [self.sam_L, self.sam_a, self.sam_b]
        xy = colour.XYZ_to_xy(XYZ)
        return xy
    
    ### 3 methods in one
    def lab_conversion(self):
        ### cieLab to cieXYZ conversion:
        cieLab = LabColor(self.sam_L, self.sam_a, self.sam_b)
        cieXYZ = convert_color(color=cieLab, target_cs=XYZColor)
        
        ### cieXYZ to RGB conversion
        rgb = convert_color(color=cieXYZ, target_cs=AdobeRGBColor)
        
        ###lab to hex-String
        hexCon = BaseRGBColor(self.sam_L, self.sam_a, self.sam_b)
        hexStr = hexCon.get_rgb_hex()
        return hexStr, cieXYZ, rgb
        

   

### outputs
#m = FarbmetrikTools1(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#hexS, xyz, labToRGB = m.lab_conversion()

#print(labToRGB)


#measE2000 = FarbmetrikTools1(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#delE2000 = measE2000.DeltaE2000()

#print(delE2000)


#measE1976 = FarbmetrikTools1(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#delE = measE1976.DeltaE1976()

#print(delE)


#measEcmc = FarbmetrikTools1(50.66, -19.09, -34.66,64.68, 45.01, 73.37)
#delEcmc = measEcmc.DeltaECMC()

#print(delEcmc)

###cie_hue out:
    ### Achtung:  Mit negativen Werten gibts eine Fehlermeldung: invalid value encountered in sqrt
    ### sqrt_Y_Y_n = np.sqrt(Y_Y_n)
    ### Nachteil derzeit: doppelte Angabe der XYZ Werte, da Class nur Eingabe von 6 Werten erlaubt.
#cie_hue = FarbmetrikTools1(50.66, 19.09, 34.66, 50.66, 19.09, 34.66)
#cie_hue = cie_hue.cie_hue()


    
