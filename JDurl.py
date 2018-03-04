#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    ReUrl
Author:    Mrtutu
Date:    2018/2/26
Description:
------------------------------------

"""
import urllib.request
import re

def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)

    pat1 = '<ul class="gl-warp clearfix">.+?<div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]

    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)

    x = 1
    for imageurl in imagelist:
        print("开始抓取第"+str(page)+"页"+"第"+str(x)+"张图片.....")
        imagename = "image/" + str(page) + str(x) + ".jpg"
        imageurl = 'http://' + imageurl

        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
            print("抓取完成!!!")
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1

        x += 1


for i in range(1, 13):
    url = 'https://list.jd.com/list.html?cat=670,671,672&page='+str(i)
    craw(url, i)