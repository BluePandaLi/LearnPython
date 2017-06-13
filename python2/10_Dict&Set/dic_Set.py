d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d
print d['Michael']

d["Michael"] = 20
print d

print 'Thomas' in d
print d.get('Thomas', -1) 

d['Thomas'] = 10
print d

d.pop("Michael")
print d

s = set([1, 2, 3, 3, 3, 3, 3,4])
print s

s.remove(4)
print s