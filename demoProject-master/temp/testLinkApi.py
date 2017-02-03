import testlink
import pdb
#
SERVER_URL = "http://192.168.31.33:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "3cf104e94144c956cdf3ef999318dce7"
tls = testlink.TestlinkAPIClient(SERVER_URL, DEVKEY)
print(tls.about())
print(tls.getProjects())
#获取测试计划信息
tl = tls.getTestPlanByName("3D旅游_APP", "huangyong");

#{'name': 'huangyong', 'testproject_id': '7251', 'api_key': 'b7beff6630175696b22c91f7185923cde063477709507eb2c388cf943fa43601', 'is_public': '1', 'id': '24541', 'notes': '<p>\n\t验证脚本修改测试计划结果</p>', 'active': '1', 'is_open': '1'}


#获取id
response = tls.getTestCaseIDByName("手机号码-登录按钮")
caseId =  response[0]["id"]
#修改测试计划下的结果
response = tls.reportTCResult(testplanid = 24541, testcaseid = caseId, buildid = 14, status = "f")
#pdb.set_trace()


# class TestLink:
#     SERVER_URL = "http://192.168.31.33:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
#     DEVKEY = "3cf104e94144c956cdf3ef999318dce7"
#     def connectTestLink(self):
#         self.testLinkInstance = testlink.TestlinkAPIClient(TestLink.SERVER_URL, TestLink.DEVKEY)
#         return self.testLinkInstance
#
#     def get_testCase_id_by_name(self, name):
#         response = self.testLinkInstance .getTestCaseIDByName(name)
#         id = response[0]["id"]
#         return id
#
#     def set_reuslt_for_case(self, testplanid, testCaseId, buildId, status="f"):
#         response = self.testLinkInstance.reportTCResult(testplanid = testplanid, testcaseid = testCaseId, buildid = buildId, status = status)
#         print(response)
