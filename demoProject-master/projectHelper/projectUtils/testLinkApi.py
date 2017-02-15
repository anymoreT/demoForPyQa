import testlink
import pdb

class TestLink(object):
    SERVER_URL = "http://192.168.31.33:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    DEVKEY = "3cf104e94144c956cdf3ef999318dce7"
    def __init__(self):
        self.project_id = None
        self.plan_id = None
        self.build_id = None

    def connectTestLink(self):
        self.testLinkInstance = testlink.TestlinkAPIClient(TestLink.SERVER_URL, TestLink.DEVKEY)
        return self.testLinkInstance

    def get_testCase_id_by_name(self, name):
        response = self.testLinkInstance .getTestCaseIDByName(name)
        id = response[0]["id"]
        return id

    def set_reuslt_for_case(self, testCaseId, testPlanId, buildId, status="f"):
        response = self.testLinkInstance.reportTCResult(testplanid = testPlanId, testcaseid = testCaseId, buildid = buildId, status = status)
        return response

    def get_cases_by_plan_name(self, project_name = "3D旅游_APP", plan_name = "API验证"):
        if self.plan_id is None:
            self.testPlan = self.testLinkInstance.getTestPlanByName(project_name, plan_name);
            self.plan_id = self.testPlan[0]["id"]
        self.testPlanCases = self.testLinkInstance.getTestCasesForTestPlan(testplanid= self.plan_id )
        return  self.testPlanCases

    def get_case_id_by_external_id(self, case_full_external_id, project_name = "3D旅游_APP", plan_name = "API验证"):
        cases = self.get_cases_by_plan_name(project_name, plan_name)
        for key, value in cases.items():
            if value[0]["full_external_id"] == case_full_external_id:
                return  key
        raise Exception("couldn't find the id of case%s"%(case_full_external_id))

    def getBuildsForTestPlan(self,project_name = "3D旅游_APP", plan_name = "API验证"):
        self.testPlan = self.testLinkInstance.getTestPlanByName(project_name, plan_name);
        self.testPlanBuilds = self.testLinkInstance.getBuildsForTestPlan(testplanid=int(self.testPlan[0]["id"]))
        return self.testPlanBuilds

    def getBuildIdOfPlan(self, project_name = "3D旅游_APP", plan_name = "API验证", build_name= "RT100"):
        builds = self.getBuildsForTestPlan(project_name, plan_name)
        for build in builds:
            if build['name'] == build_name:
                return int(build['id'])
        raise Exception("couldn't find the build")

    def get_plan_info(self, project_name = "3D旅游_APP", plan_name = "API验证", build_name= "RT100"):
        self.testPlan = self.testLinkInstance.getTestPlanByName(project_name, plan_name);
        self.plan_id = int(self.testPlan[0]["id"])
        self.project_id = int(self.testPlan[0]["testproject_id"])
        self.build_id = self.getBuildIdOfPlan( project_name , plan_name , build_name)


    def updata_result_for_testCase(self,case_full_external_id, status, project_name = "3D旅游_APP", plan_name = "API验证", build_name= "RT100"):
        if (self.plan_id is None) or (self.build_id  is None):
            self.get_plan_info(project_name, plan_name, build_name)
        testCaseId = self.get_case_id_by_external_id(case_full_external_id, project_name, plan_name )
        self.set_reuslt_for_case(testCaseId = testCaseId, testPlanId = self.plan_id, buildId = self.build_id, status = status )