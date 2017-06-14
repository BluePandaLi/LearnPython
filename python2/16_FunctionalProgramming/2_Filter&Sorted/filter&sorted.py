#coding utf-8
#filter
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])
print '\n'

def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print '\n'

#sorted
print sorted([36, 5, 12, 9, 21])
print '\n'

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)
print '\n'

def f(x):
    return x.upper()
print sorted(map(f,['bob', 'about', 'Zoo', 'Credit']))
print '\n'

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)