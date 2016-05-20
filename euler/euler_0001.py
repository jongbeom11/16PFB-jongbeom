#-*-coding: cp949 -*-
#-*-coding: utf-8 -*-


#1000이하의 숫자에서 3에 배수를 더하는 과정
sum3 = 0
for i in range(1,334):
    sum3 = sum3 + 3*i
print (sum3)

#1000이하의 숫자에서 5의 배수를 더하는 과정
sum5 = 0
for i in range(1,201):
    sum5 = sum5 + 5*i
print (sum5)

#따라서 sum3은 1000이하의 숫자에서 3의 배수를 더한값
#       sum5는 1000이하의 숫자에서 5의 배수를 더한값

print sum3+sum5