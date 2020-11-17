# -*- coding: utf-8 -*-
"""
Created on Sun Dec 1 14:59:34 2019

@author: Weihao XIA (Will Hsia)
"""

import os
 
def dirpath(lpath, lfilelist):
    list = os.listdir(lpath)
    for f in list:
        file = os.path.join(lpath, f)
        if os.path.isdir(file):      
            dirpath(file, lfilelist)
        else:
            lfilelist.append(file)
    return lfilelist

filename = 'gaze_train.txt' 
path = 'H:/Gaze/Gaze_Code/gaze_redirection/dataset/all'

lfilelist = dirpath(path, [])

file = open(filename,'a') 

for f in lfilelist:
    f = os.path.split(f)[1]
    file.write(f+'\n')
file.close()
print("Success!")