#coding: utf-8

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#@log
def now():
    print '2013-12-25'

now = log(now)
now()
print '\n'

#这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator).
#本质上，decorator就是一个返回函数的高阶函数.
print 'using decorator'
@log
def now2():
    print '2017.6.14'
now2()
