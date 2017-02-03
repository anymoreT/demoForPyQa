from functools import wraps,partial
import  pdb
from . import  testLinkApi
def getIdByTestLinkName(caseName):
    if callable(caseName):  # 参数如果是函数，说明装饰器不带参传过来,text是一个函数
        @wraps(caseName)
        def wrapper(*args, **kwargs):
            print("这是不带参数的装饰器,开始执行")
            f = caseName(*args, **kwargs)  #执行本身的函数 text（）
            return f  # 返还原函数
        return wrapper
    elif not callable(caseName):  # text是参数，不是函数
        testCaseName =  caseName
        def decarator(func):
            @wraps(func)
            def warpper(*args, **kwargs):
                pdb.set_trace()
                print(testCaseName)
                testLinkInstance = testLinkApi.TestLink()
                testLinkInstance.connectTestLink()
                id = testLinkInstance.get_testCase_id_by_name(testCaseName)
                f = func(*args, **kwargs)
                return f  #返还原函数
            return warpper
        return decarator
    else:
        print("请检查是否正确")




