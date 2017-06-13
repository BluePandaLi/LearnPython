#coding utf-8
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0], classmates[1], classmates[2]
print classmates[-1], classmates[-2], classmates[-3]
# print classmates[4]
# print classmates[3]
classmates.append('Adam')
print classmates

classmates.insert(1, 'Adam')
print classmates

classmates.pop()
print classmates

classmates.pop(0)
print classmates

classmates[0] = 'Michael'
print classmates

classmates[1] = True
print classmates

classmates.append(['123', 432])
print classmates