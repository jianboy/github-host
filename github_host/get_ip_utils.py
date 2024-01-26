#!/usr/bin/env python





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
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36',
               'Host': 'ip-api.com'}
    url = "http://ip-api.com/json/%s?lang=zh-CN" % (site)
    trueip = None
    for i in range(5):
        try:
            res = requests.get(url, headers=headers, timeout=5)
            res = json.loads(res.text)
            if(res["status"] == "success") and len(re.findall(r"\b(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}\b", res["query"])) == 1:
                trueip = res["query"]
                break
        except Exception as e:
            print("查询" + site + " 时出现错误: " + str(e))
    return trueipf
