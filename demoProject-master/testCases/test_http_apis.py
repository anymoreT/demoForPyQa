# -*- coding:utf-8 -*-
import unittest 
from pyQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.log.log import Log
import pdb
from pyQa.utils.tools import  Tools


class TestApis(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("project.ymal")
        self.case_data = PUtils.get_project_config("case_data.ymal")
        self.env = Tools.get_test_suit_env()


    @unittest.skipUnless(Tools.runCaseIn("smoke", "smoke"), "skip case if not in tags")
    def test_TC001(self):
        Log.log_case_desc("Api:/service/index.php/user/login/loginByPhoneNum，响应是200")
        http_handle = HttpHandle()
        login_url = "http://" + self.config["Host"][self.env] + self.config["Victy"]["Login"]
        #data = {"phoneNum":"13980845431", "pwd":"huang12345"}
        data = eval(self.case_data["TC001"]["Data"])
        http_handle.do_post(login_url, data)
        http_handle.response_code_status_should_be(200)
        http_handle.print_response_body()

    @unittest.skipUnless(Tools.runCaseIn("smoke", "smoke"), "skip case if not in tags")
    def test_TC002(self):
        Log.log_case_desc("Api:/service/index.php/user/login/loginByPhoneNum，输入错误号码，登录失败")
        http_handle = HttpHandle()
        login_url = "http://" + self.config["Host"][self.env] + self.config["Victy"]["Login"]
        #data = {"phoneNum":"13980845431", "pwd":"huang12345"}
        data = eval(self.case_data["TC001"]["Data1"])
        http_handle.do_post(login_url, data)
        http_handle.response_string_should_include("true")
        http_handle.print_response_body()
        
 