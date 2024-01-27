#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2019/08/03 16:16:59
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   refeash github host everyday
'''
import os
import datetime
from github_host import get_ip_utils
from github_host.libs.json_conf import JsonConf


class Github(object):

    def __init__(self):
        self.jsonConf = JsonConf()
        self.conf = self.jsonConf.load()
        self.sites = self.conf.get('sites')
        self.addr2ip = {}
        self.hostLocation = r"hosts"

    def dropDuplication(self, line):
        flag = False
        if "#*******" in line:
            return True
            for site in self.sites:
                if site in line:
                    flag = flag or True
                else:
                    flag = flag or False
        return flag

    def saveRouterosFile(self):
        ''' 应网友需求，导出一份 routeros 格式的hosts文件 '''
        today = datetime.date.today()
        with open("hosts-routeros.txt", "w") as f:
            f.write("#*********************github " +
                    str(today) + " update********************\n")
            f.write(
                "#******* get latest hosts: http://blog.yoqi.me/lyq/16489.html/n")
            for key in self.addr2ip:
                f.write("add address=" + self.addr2ip[key] + " name="+ key + "\n")

    # 更新host, 并刷新本地DNS
    def updateHost(self):
        today = datetime.date.today()
        for site in self.sites:
            trueip = get_ip_utils.getIpFromipapi(site)
            if trueip != None:
                    self.addr2ip.append[site] = trueip[0]
            with open(self.hostLocation, "r") as f1:
                    f1_lines = f1.readlines()
                    with open("temphost", "w") as f2:
                        for line in f1_lines:                       # 为了防止 host 越写用越长，需要删除之前更新的含有github相关内容 
                            result=self.dropDuplication(line)
                                if self.dropDuplication(line) == False:
                                    f2.write(line)
                        f2.write("#*********************github " +
                                str(today) + " update********************\n")
                        for key in self.addr2ip:
                            for newhosts in range(len(trueip)):
                                f2.write(self.addr2ip[key] + "\t" + trueip[newhosts] + "\n")
        os.remove(self.hostLocation)
        os.rename("temphost", self.hostLocation)
        # os.system("ipconfig /flushdns")
        self.saveRouterosFile()
