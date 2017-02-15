from projectHelper.projectUtils.testLinkApi import TestLink

testLinkInstance = TestLink()
testLinkInstance.connectTestLink()
# cases = testLinkInstance.get_cases_by_plan_name()
# for key,value in cases.items():
#     print(key)
#     print(value[0])
# print(len(cases))
#
# builds = testLinkInstance.getBuildsForTestPlan()
# build_id = testLinkInstance.getBuildIdOfPlan()
# print(build_id)
# testLinkInstance.get_plan_info()
# id = testLinkInstance.get_case_id_by_external_id("3D旅游_APP-180")
# print("case id:", id)
testLinkInstance.updata_result_for_testCase("3D旅游_APP-180", "f")
testLinkInstance.updata_result_for_testCase("3D旅游_APP-180", "p")