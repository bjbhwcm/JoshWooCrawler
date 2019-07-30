# -*- coding: utf-8 -*-

#author joshwoo
import json
import base64
from urllib import request
import urllib
import re

global_url = "https://photo.sina.com.cn/"
username=""
password=""
pic_suffix = [".jpg",".png",".jpeg",".JPG",".JPEG",".PNG",".gif",".GIF",]

def get_resp(url):
    resp = urllib.request.urlopen(url)
    return  resp

def get_all_urls(resp_str):
    seacheDict = {}
    seacheObj = re.search(r'\"(.*)\"',resp_str,re.M|re.I)
    if seacheObj:
        seacheDict = seacheObj.groupdict()
    for i in seacheDict:
        print(i)

#def get_suffix(s):


#def getPic():

if __name__ == "__main__":
   res = get_resp(global_url).read().decode("utf-8")
   get_all_urls(res)