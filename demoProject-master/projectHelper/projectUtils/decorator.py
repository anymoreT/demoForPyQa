from functools import wraps,partial
import  pdb

import   unittest
def RecordResult(caseName):
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
                print(testCaseName)
                try:
                   func(*args, **kwargs)
                finally:
                    id = args[0].id()
                    print("++++++++++++++++++++++++++++++++++++++++after result:")
                    print( id )


            return warpper
        return decarator
    else:
        print("请检查是否正确")




