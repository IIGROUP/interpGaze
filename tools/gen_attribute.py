# -*- coding: utf-8 -*-
"""
Created on Sun Dec 1 14:59:34 2019

@author: Weihao XIA (Will Hsia)
"""

import os, csv

headers = ['name','0P','15P','-15P','30P', '-30P','0V','10V','-10V','15V','-15V','0H','10H','-10H','15H','-15H','L','R'] 
f = open('gaze.csv','rb+')

path = "/Users/will/Downloads/Gaze/Gaze_Redirection/dataset/all"

f_csv = csv.DictWriter(f, headers)
f_csv.writeheader()
writer = csv.writer(f, dialect='excel' ,lineterminator='\n')

for path, dirs, files in os.walk(path):
 	for filename in files:
 		each_row = [-1]*(len(headers)-1)
 		f_n = filename.split('.')[0].split('_')
		for (i, head) in list(enumerate(headers[1:])):
			for j in [2,3,4,5]:
				if f_n[j] == head:
					each_row[i] = 1
		writer.writerow([filename] + each_row)
f.close()