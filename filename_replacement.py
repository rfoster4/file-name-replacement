# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
# Change rootdir path to folder containing files that you wish to edit
rootdir = r'C:\scratch_2019'
# Change str to charachter or string you would like to remove
str = " "
for filename in os.listdir(rootdir):
    if str in filename:    
        filepath = os.path.join(rootdir, filename)
        # filename.replace(str, "CHARACTER OR STRING YOU WOULD LIKE TO REPLACE WITH")
        newfilepath = os.path.join(rootdir, filename.replace(str, ""))
        os.rename(filepath, newfilepath)
print(filename)
print("Finished!")

