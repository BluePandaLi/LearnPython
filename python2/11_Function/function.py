import math

print abs(100)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-100)

def nop():
    pass

# print my_abs(1,2)
# print my_abs("50")

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print move(10, 20, 3)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1,2,3,4)
print calc()

l = [1,2,3,4,5]
print calc(*l)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person("Michael", 30, country = 'China', gender = 'M', job = 'Engineer')

d = {"country": 'China', "gender" : 'M', "job" : 'Engineer'}
# ** deduce
# person("Michael", 30, d)
person("Michael", 30, **d)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(100)
# stack overflow
# print fact(1000)