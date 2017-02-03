# -*- coding:utf-8 -*-
from pyQa.utils.tools import Tools
import os
import hashlib
import pdb
import datetime
import  hmac
import base64

class PUtils(object):
    @staticmethod
    def get_project_config(config_file = "config.ymal"):
        #读取project_config下面的文件夹里面的项目配置数据
        config_path = os.path.dirname(__file__)
        config_path = os.path.join(config_path, "test_config", config_file)
        return Tools.get_config(config_path)

    def registe_user(phone, password):
        pass

    @classmethod
    def md5String(cls, origin_str):
        md5Instance = hashlib.md5()
        md5Instance.update(origin_str.encode())
        hexString = md5Instance.hexdigest()
        print("test class method")
        print(hexString)
        return hexString

    @classmethod
    def sha256String(cls, origin_str):
        secret = "D372A31BE6567A4E24065903D8CC8E62848CE533EC0BD024574ABB8646388B54".encode()
        hexString = hmac.new(secret, origin_str.encode(), digestmod=hashlib.sha256).digest()
        hexString = base64.encodebytes(hexString)
        print(hexString.decode())
        return hexString

    @classmethod
    def get_utc_date_str(cls, format ="%Y-%M-%dT%H:%M:%SZ" ):
        utc_date = datetime.datetime.utcnow()
        str = utc_date.strftime(format)
        print(str)
        return