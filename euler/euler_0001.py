#-*-coding:utf8
A = [x for x in range(1, 1000) if x % 5 == 0] #5의 배수를 1에서 1000까지의 범위 내에서 찾습니다.
print (A) #위의 결과값을 출력합니다.

B = [x for x in range(1, 1000) if x % 3 == 0] #3의 배수를 1에서 1000까지의 범위 내에서 찾습니다
print (B) #위의 결과값을 출력합니다.

C = [x for x in range(1, 1000) if x % 15 == 0] #3과 5의 최소 공배수인 15의 배수를 1에서 1000사이에서 찾습니다.
print (C) #위의 결과값을 출력합니다.

S = sum(A+B)-sum(C) #5의 배수와 3의 배수를 모두 더한후 2번 더해진 3과 5의 최소 공배수의 배수 즉, 15의 배수를 한번 빼줍니다.
print (S) #위의 값을 출력해 줍니다.