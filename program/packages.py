# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:24:30 2020

@author: SePa
"""
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# call packages you want to install
if __name__ == '__main__':
    install('colour-science')

