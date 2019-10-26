# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:45:19 2018

@author: Lakshmikanth
"""

# Code to download from list of links:
import pandas as pd

from urllib.requet import urlopen
# Option for saving original name, see below
# from os.path import basename

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
# Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
# Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'


data=pd.read_csv("Images_Train.csv")

data.head()

i=0
for line in data.Link_to_the_image:
    if line != 'nan':               # if in the list there are any empty cells
        try:
            res = urlopen(line)
            imgData = res.read()
            # Option to save the original file name to later transfer products in a CSV file etc
            # output = open("Images/" + str(basename(res.url)) + ".png",'wb')
            output = open("Images/img_" + str(i) + ".png", 'wb')
            output.write(imgData)
        except:
            print("Exception")
    else:
        print ("Image not found".format(line))
    print(i)
    i=i+1
print('complete')
