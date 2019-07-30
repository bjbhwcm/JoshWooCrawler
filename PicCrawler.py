# -*- coding: utf-8 -*-

#author joshwoo
from urllib import request
import urllib
import re
import os
import time
import hashlib

global_url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87"
username=""
password=""
pic_suffix = [".jpg",".png",".jpeg",".JPG",".JPEG",".PNG",".gif",".GIF",]
savepath = os.getcwd() + "\\picture\\"

def get_resp(url):
    try:
        resp = urllib.request.urlopen(url)
        return  resp
    except Exception:
        return None

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

def getPic(pic_url_dict,):
    m = hashlib.md5()
    for i in pic_url_dict:
        m.update(str(time.time()).encode("utf-8"))
        pic_name = savepath + "\\"+ m.hexdigest() + get_pic_suffix(i)
        res = get_resp(i)
        if res is not None:
            f = open(pic_name,"wb")
            f.write(res.read())
            f.close()

#def get_recur_urls(other_url_dict):


def crawl_pics(global_url):
    res = get_resp(global_url)
    if res is None:
        return None
    try:
        res_str = res.read().decode("utf-8")
    except Exception:
        return None
    all_urls_dict = get_all_urls(res_str)
    if len(all_urls_dict) == 0:
        return None
    pic_url_dict, other_url_dict = get_urls_with_pic_suffix(all_urls_dict)
    if len(pic_url_dict) == 0:
        return None
    getPic(pic_url_dict)
    if len(other_url_dict) == 0:
        return None
    for i in other_url_dict:
        crawl_pics(i)

if __name__ == "__main__":
    crawl_pics(global_url)
