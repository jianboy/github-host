#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2019/08/03 17:02:15
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   get ip from ip address
'''

from email import header
import requests
from bs4 import BeautifulSoup
import re
import json


def getIpFromIpaddress(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ipaddress.com'}
    url = "https://sites.ipaddress.com/" + site
    trueip = None
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        ip = re.findall(r"\b(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}\b", res.text)
        result = soup.find_all({'class':'origin'})
        for c in result:
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip


def getIpFromChinaz(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ipw.cn'}
    url = "http://ipw.cn/ipv6webcheck/?site=" + site
    trueip = None
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', {"target": "_blank"})
        for c in result:
            ip = re.findall(r"\b(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}\b", c.text)
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip


def getIpFromWhatismyipaddress(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip.tool.chinaz.com'}
    url = "https://whatismyipaddress.com//hostname-ip"
    data = {
        "DOMAINNAME": site,
        "Lookup IP Address": "Lookup IP Address"
    }
    trueip = None
    try:
        res = requests.post(url, headers=headers, data=data, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', class_="Whwtdhalf w15-0")
        for c in result:
            ip = re.findall(r"\b(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}\b", c.text)
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip


def getIpFromipapi(site):
    '''
    return trueip: None or ip
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4844.51 Safari/537.36',
               'Host': 'sites.ipaddress.com'}
    url = "https://sites.ipaddress.com/" + site
    trueip = None
    try:
        print (url)
        res = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all(id='tabpanel-dns-aaaa')
        print (result)
        for c in result:
            trueip = re.findall(r'(?:\w{0,4}\:){5,7}\w{0,4}', c.text)
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip
