#-*-coding:utf8
#http://learnpythonthehardway.org/book/ex33.html

i = 0
number = []

while i < 6:
    print ("At the top i is %d" % i)
    number.append(i)

    i = i + 1

    print ("Numbers now:" + str(number))
    print ("At the bottom i is %d" % i)

print ("The numbers: ")

for num in number:
    print (num)