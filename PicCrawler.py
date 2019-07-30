# -*- coding: utf-8 -*-

#author joshwoo
import json
import base64
from urllib import request
import urllib
import re
import datetime
import os
import time

global_url = "https://photo.sina.com.cn/"
username=""
password=""
pic_suffix = [".jpg",".png",".jpeg",".JPG",".JPEG",".PNG",".gif",".GIF",]
savepath = os.getcwd() + "\\picture\\"
pic_count = 0

def get_resp(url):
    resp = urllib.request.urlopen(url)
    return  resp

def get_all_urls(resp_str):
    redict = []
    seacheObj = re.findall(r'\"http(.[^\"]*)\"',resp_str,re.M|re.I)
    for i in seacheObj:
        s = "http"+i
        redict.append(s)
    return  redict

def get_pic_suffix(s):
    n = len(s) - 1
    res = ""
    flag = False
    for i in range(n + 1):
        res = res + s[n]
        if s[n] == ".":
            flag = True
            break
        n = n - 1
    if flag:
        suffix = res[::-1]
        if suffix in pic_suffix:
            return suffix
        else:
            return None
    else:
        return None

def get_urls_with_pic_suffix(url_dict):
    pic_urls = []
    other_urls = []
    for i in url_dict:
        suffix = get_pic_suffix(i)
        if suffix:
            pic_urls.append(i)
        else:
            other_urls.append(i)
    return pic_urls,other_urls

def getPic(pic_url_dict,pic_count):
    for i in pic_url_dict:
        pic_name = savepath + "\\"+ str(pic_count) + get_pic_suffix(i)
        res = get_resp(i)
        f = open(pic_name,"wb")
        f.write(res.read())
        f.close()
        pic_count = pic_count + 1

def crawl_pics(global_url):
    res = get_resp(global_url).read().decode("utf-8")
    all_urls_dict = get_all_urls(res)
    pic_url_dict, other_url_dict = get_urls_with_pic_suffix(all_urls_dict)
    getPic(pic_url_dict,pic_count)


if __name__ == "__main__":
   res = get_resp(global_url).read().decode("utf-8")
   all_urls_dict = get_all_urls(res)
   pic_url_dict,other_url_dict = get_urls_with_pic_suffix(all_urls_dict)
   getPic(pic_url_dict,pic_count)