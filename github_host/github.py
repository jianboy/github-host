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
        self.trueip = []

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
            for key in range(0, len(self.trueip), 2):
                f.write(self.trueip[key] + "\t" + self.trueip[key+1] + "\n")

    # 更新host, 并刷新本地DNS
    def updateHost(self):
        today = datetime.date.today()
        for site in self.sites:
            ips = get_ip_utils.getIpFromipapi(site)
            if ips:  # 检查 ips 是否不为 None 且为非空列表
                for key in ips:
                    self.trueip.extend([key, site])
        with open(self.hostLocation, "r") as f1:
            f1_lines = f1.readlines()
            with open("temphost", "w") as f2:
                for line in f1_lines:         # 为了防止 host 越写用越长，需要删除之前更新的含有github相关内容
                    if self.dropDuplication(line) == False:
                        f2.write(line)
                f2.write("#*********************github " +
                     str(today) + " update********************\n")
                for key in range(0, len(self.trueip), 2):
                    f2.write(self.trueip[key] + "\t" + self.trueip[key+1] + "\n")
        os.remove(self.hostLocation)
        os.rename("temphost", self.hostLocation)
        # os.system("ipconfig /flushdns")
        self.saveRouterosFile()
