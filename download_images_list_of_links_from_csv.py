# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:45:19 2018

@author: Lakshmikanth
"""

# Code to download from list of links:
# import pandas as pd

from urllib2 import urlopen

data=pd.read_csv("Images_Train.csv")

data.head()

i=0
for line in data.Link_to_the_image:
    if line != 'nan':               # if in the list there are any empty cells
    try: 
        res = urlopen(line)
        imgData = res.read()
        output = open("Images/img_" + str(i) + ".png",'wb')
        output.write(imgData)
    except:
        print("Exception")
    else:
        print ("Image not found".format(line))
    print(i)
    i=i+1
print('complete')