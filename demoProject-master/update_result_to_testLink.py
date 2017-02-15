import  xml.dom.minidom
from  os import  path
import  pdb


def get_result_dict(itemList):
    resutl_dic = {}
    nodes = itemlist[0].childNodes
    for node in nodes:
        if ("testcase" == node.nodeName):
            name =  node.getAttribute("name")
            #默认值passed
            resutl_dic[name] = "passed"
            childNodes = node.childNodes
            if len(childNodes) > 0:
                for childNode in childNodes:
                    if ("failure" == childNode.nodeName):
                        resutl_dic[name] = "failure"
    return resutl_dic


path_dir = path.dirname(__file__)
xml_path = path.join(path_dir, "report", "xml_result.xml")
print(xml_path)
#打开xml文档
dom = xml.dom.minidom.parse(xml_path)
#得到文档元素对象
root = dom.documentElement
itemlist = root.getElementsByTagName('testsuite')
print(get_result_dict(itemlist))