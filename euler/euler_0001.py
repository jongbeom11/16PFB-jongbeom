#-*- coding: utf-8 -*-
a = range(1,10)
b = range(1,1000)

# 3 또는 5 의 배수 와 그의 합
e = []
for c in a :
    if c%3 == 0 :
        e.append(c)
for d in a :
    if d%5 == 0 :
        e.append(d)
print e
f = sum(e)
print(f)

# 1000 미만 3 또는 5의 배수의 합
g =[]
for h in b :
    if h%3 == 0 :
        g.append(h)
        # b에서 3으로 나누어서 나머지가 0인 숫자는 h 이다.
        # g에 h 를 추가한다
for i in b :
    if i%5 == 0 :
        g.append(i)
        # b에서 5로 나누어서 나머지가 0인 숫자는 i 이다.
        # g에 i 를 추가한다
print g
j = sum(g)
# j는 g의 합
print(j)