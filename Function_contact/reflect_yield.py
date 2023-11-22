from Function_contact import def_Readfunction

'''
    getattr(实例化对象名称，属性名称) 
    getattr(实例化对象名称，方法名称)()，调用方法
    不存在的会报错，用 try except traceback 获取报错内容
    
    setattr(实例化对象名称，属性名称)
    
    hasattr(实例化对象名称，属性名称)  返回True False 查看是否有该属性
    
    delattr(只能是类名，属性名称) 删除了绑定的方法名称，导致不能调用，当前堆栈里面所有的该类的对象都不能使用
    
    iter()
    把list对象转化为迭代器对象
    
'''

test_01 = def_Readfunction.WriteFunction('../../directory/test02', '新写点什么')

try:
    getattr(test_01, 'for_use')()
except:
    print
