import  xml.dom.minidom
from  os import  path
import  pdb
from projectHelper.projectUtils.testLinkApi import TestLink


def get_result_dict(itemList):
    resutl_dic = {}
    nodes = itemlist[0].childNodes
    for node in nodes:
        if ("testcase" == node.nodeName):
            name =  node.getAttribute("name")
            #默认值passed
            resutl_dic[name] = {}
            resutl_dic[name]['status'] = "p"
            childNodes = node.childNodes
            if len(childNodes) > 0:
                for childNode in childNodes:
                    if ("failure" == childNode.nodeName):
                        resutl_dic[name]['status'] = "f"
    return resutl_dic


path_dir = path.dirname(__file__)
xml_path = path.join(path_dir, "report", "xml_result.xml")
print(xml_path)

#打开xml文档
dom = xml.dom.minidom.parse(xml_path)
#得到文档元素对象
root = dom.documentElement
itemlist = root.getElementsByTagName('testsuite')

dic1 = get_result_dict(itemlist)
print(dic1)

#将测试转换成testlink的extern_id
case_extern_id_pre = "3D旅游_APP-"
for key in dic1.keys():
    test_case_extern_id = case_extern_id_pre + key.split("test_APP_")[1]
    dic1[key]["test_case_extern_id"] = test_case_extern_id
print(dic1)


testLinkInstance = TestLink()
testLinkInstance.connectTestLink()
#更新结果
for key in dic1.keys():
    testLinkInstance.updata_result_for_testCase(dic1[key]["test_case_extern_id"], dic1[key]["status"],build_name= "RT101")

