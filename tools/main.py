
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   liuyuqi
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2020/04/26 23:01:40
@Version :   1.0
@License :   Copyright © 2017-2020 liuyuqi. All Rights Reserved.
@Desc    :   github.com
'''

import shutil
import os,sys,ctypes
import datetime
import get_ip_utils
import platform

# 需要获取ip的网址
sites = [
    "github.global.ssl.fastly.net",
    "assets-cdn.github.com",
    "documentcloud.github.com",
    "gist.github.com",
    "gist.githubusercontent.com",
    "github.githubassets.com",# 很卡
    "help.github.com",
    "nodeload.github.com",
    "raw.github.com",
    "status.github.com",
    "training.github.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars6.githubusercontent.com",
    "avatars7.githubusercontent.com",
    "avatars8.githubusercontent.com",
    "codeload.github.com",
    "camo.githubusercontent.com",
    "raw.githubusercontent.com", 
    "cloud.githubusercontent.com",
    "user-images.githubusercontent.com",
    "customer-stories-feed.github.com",
    "pages.github.com",
    "api.github.com",
    "live.github.com",
    "githubapp.com",
    "github.com"
]

addr2ip = {}
hostLocation = r"hosts"

def dropDuplication(line):
    flag = False
    if "#*********************github" in line:
        return True
    for site in sites:
        if site in line:
            flag = flag or True
        else:
            flag = flag or False
    return flag

# 更新host, 并刷新本地DNS
def updateHost():
    today = datetime.date.today()
    for site in sites:
        trueip=get_ip_utils.getIpFromipapi(site)
        if trueip != None:
            addr2ip[site] = trueip
            print(site + "\t" + trueip)
    with open(hostLocation, "r") as f1:
        f1_lines = f1.readlines()
        with open("temphost", "w") as f2:
            for line in f1_lines:                       # 为了防止 host 越写用越长，需要删除之前更新的含有github相关内容
                if dropDuplication(line) == False:
                    f2.write(line)
            f2.write("#*********************github " +
                     str(today) + " update********************\n")
            for key in addr2ip:
                f2.write(addr2ip[key] + "\t" + key + "\n")
    os.remove(hostLocation)
    os.rename("temphost",hostLocation)

if __name__ == "__main__":
    updateHost()
