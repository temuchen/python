__author__ = 'temuchen'
# -*- coding: utf-8 -*-
import os

for root,dirs,files in os.walk('c:\\pro\\test'):
        for name in files:
            if not name.endswith(".txt") and not name.endswith(".docx") or files == []:
                os.remove(os.path.join(root,name))
                print("Delete File:"+os.path.join(root,name))


for root,dirs,files in os.walk('c:\\pro\\test'):
    for subdir_item in dirs:
        dir_path = os.path.join(root,subdir_item)
        if len(os.listdir(dir_path))==0:
            os.rmdir(dir_path)
            print("Delete Dir:"+dir_path)


os.system("pause")
