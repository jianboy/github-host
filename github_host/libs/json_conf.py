#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/05/24 15:07:14
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   yaml util
'''
import os
import json


class JsonConf:
    def __init__(self, config_path="conf/config.json"):
        self.config_path = config_path

    def save(self, data):
        with open(self.config_path, 'w') as json_file:
            json_file.write(json.dumps(data, indent=4))

    def load(self):
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as json_file:
                pass
        with open(self.config_path, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except Exception as e:
                if(str(e).index("utf-8-sig") > 0):
                    with open(self.config_path, encoding="utf-8-sig") as json_file:
                        data = json.load(json_file)
                        return data
                else:
                    print(e)
            return data

    def set(self, data_dict):
        json_obj = self.load()
        for key in data_dict:
            json_obj[key] = data_dict[key]
        self.save(json_obj)
        print(json.dumps(json_obj, indent=4))

    def get(self, key, default_val=""):
        '''
        配置文件获取key对象的值，如果没有设置就返回默认值
        '''
        try:
            result = self.load()[key]
            return result
        except Exception as e:
            print(e)
            return default_val

    def get(self, jsonData, key, default_val=""):
        try:
            return jsonData[key]
        except Exception as e:
            return default_val

    @staticmethod
    def get(jsonData, key, default_val=""):
        try:
            return jsonData[key]
        except Exception as e:
            return default_val
