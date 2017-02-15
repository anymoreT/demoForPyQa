# -*- coding:utf-8 -*-
import unittest
from pyQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.log.log import Log
import pdb
from pyQa.utils.tools import  Tools
from projectHelper.projectUtils.decorator import  RecordResult


class TestApis(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("project.ymal")
        self.case_data = PUtils.get_project_config("case_data.ymal")
        self.env = Tools.get_test_suit_env()
        print("+++++++++setUp")




   # @RecordResult("非法用户不能成功登录app")
    @unittest.skipUnless(Tools.runCaseIn("smoke", "smoke"), "skip case if not in tags")
    def test_APP_180(self):
        Log.log_case_desc("非法用户不能成功登录app")
        http_handle = HttpHandle()
        login_url = "http://" + self.config["Host"][self.env] + self.config["Victy"]["Login"]
        #检查错误的电话号码
        data = eval(self.case_data["APP_180"]["illegal_phone_num"])
        http_handle.do_post(login_url, data)
        http_handle.response_code_status_should_be(200)
        http_handle.response_dictionary_should_have_key_value("status", False)
        http_handle.response_dictionary_should_have_key_value("data", None)
        http_handle.response_keys_type_is_right(target_struct={"status":"BOOL", "msg":"STRING"})
        http_handle.response_key_value_is_right(target_value={"status":False, "msg":"手机格式不正确", "data":None})

        #检查错误的密码
        data = eval(self.case_data["APP_180"]["wrong_password"])
        http_handle.do_post(login_url, data)
        http_handle.response_code_status_should_be(200)
        http_handle.response_key_value_is_right(target_value={"status":False, "msg":"密码错误！请检查!", "data":None})

        #检查密码为空
        data = eval(self.case_data["APP_180"]["no_password"])
        http_handle.do_post(login_url, data)
        http_handle.print_response_body()
        http_handle.print_response_python_strcut_body()
        http_handle.response_code_status_should_be(200)
        http_handle.response_key_value_is_right(target_value={"status":False, "msg":"密码错误！请检查!", "data":None})


    #@RecordResult("合法用户成功登录app")
    @unittest.skipUnless(Tools.runCaseIn("smoke", "smoke"), "skip case if not in tags")
    def test_APP_179(self):
        Log.log_case_desc("合法用户成功登录appp")
        http_handle = HttpHandle()
        login_url = "http://" + self.config["Host"][self.env] + self.config["Victy"]["Login"]
        #检查正确的电话号码
        data = eval(self.case_data["APP_179"]["right_account"])
        http_handle.do_post(login_url, data)
        http_handle.response_code_status_should_be(200)
        http_handle.print_response_python_strcut_body()
        http_handle.response_keys_type_is_right(target_struct={"status": "BOOL", "msg": "STRING", "data":"HASH"})
        http_handle.response_key_value_is_right(target_value={"status":True, "msg":"登录成功"})
        http_handle.response_keys_type_is_right("data", target_struct={"userID": "INT", "account": "STRING", "imPass":"INT"})




 