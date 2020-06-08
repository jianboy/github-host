import requests
from bs4 import BeautifulSoup
import re


def getIpFromIpaddress(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ipaddress.com'}
    url = "https://ipaddress.com/search/" + site
    trueip = None
    try:
        res = requests.get(url, headers=headers, timeout=2)
        soup = BeautifulSoup(res.text, 'html.parser')
        ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res.text)
        result = soup.find_all('div', class_="comma-separated")
        for c in result:
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip


def getIpFromChinaz(site):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip.tool.chinaz.com'}
    url = "http://ip.tool.chinaz.com/" + site
    trueip = None
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', class_="Whwtdhalf w15-0")
        for c in result:
            ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
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
        res = requests.post(url, headers=headers, data=data)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find_all('span', class_="Whwtdhalf w15-0")
        for c in result:
            ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
            if len(ip) != 0:
                trueip = ip[0]
    except Exception as e:
        print("查询" + site + " 时出现错误: " + str(e))
    return trueip
