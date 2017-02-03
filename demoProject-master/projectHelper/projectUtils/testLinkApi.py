import testlink
import pdb

class TestLink(object):
    SERVER_URL = "http://192.168.31.33:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    DEVKEY = "3cf104e94144c956cdf3ef999318dce7"
    def connectTestLink(self):
        self.testLinkInstance = testlink.TestlinkAPIClient(TestLink.SERVER_URL, TestLink.DEVKEY)
        return self.testLinkInstance

    def get_testCase_id_by_name(self, name):
        response = self.testLinkInstance .getTestCaseIDByName(name)
        id = response[0]["id"]
        return id

    def set_reuslt_for_case(self, testplanid, testCaseId, buildId, status="f"):
        response = self.testLinkInstance.reportTCResult(testplanid = testplanid, testcaseid = testCaseId, buildid = buildId, status = status)
        print(response)
