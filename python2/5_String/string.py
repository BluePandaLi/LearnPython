#coding:utf-8
print '中文'

print u'\u4e2d'

print len('abc')
print len(u'abc')
print len(u'中文')

print 'abc'.decode('utf-8')

#String format
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)