# coding=utf-8
__author__ = 'Administrator'
 
 
import os
 
 
tab=' '*4+"|"
blank=" "*5
 
# 存放当前级别目录个数
dict={}
 
# 探测目录深度
def deep(path=None):
    if path==None:
        return 0
    if path.__len__()==0:
        return 0
    arr = path.split(os.sep)
    return arr.__len__()
 
def walk(dir='.'):
    # 打印根文件夹
    pre=os.path.split(os.path.abspath(dir))[0]
    for dirpath, dirnames, filenames in os.walk(dir):
        dirpath=dirpath.replace(pre+os.sep,"")
        # print dirpath
        # print dirnames
        dirDepth=deep(dirpath)-1
        fileDepth = dirDepth+1
 
        # 存放文件夹下所有目录
        dict[dirDepth] = len(dirnames)
        # print dict
 
        if dirDepth-1>-1:
            depth = dict[dirDepth-1]
            if depth>0:
                dict[dirDepth-1] -= 1
 
        dirname=os.path.split(os.path.abspath(dirpath))[1]
        # print dirname,dirDepth
        # print tab*dirDepth+" "+dirname
        str=''
        for i in range(0,dirDepth):
                if dict[i]>0:
                    str += tab
                else:
                    str += blank
        str=str[:-1]
        str += ("|-"+dirname)
        print str
 
        # for filename in filenames:
        #     print tab*fileDepth+" "+filename
 
        for filename in filenames:
            str=''
            for i in range(0,fileDepth):
                if dict[i]>0:
                    str += tab
                else:
                    str += blank
            str=str[:-1]
            str += ("|-"+filename)
            print str