# -*-coding:utf8
#http://learnpythonthehardway.org/book/ex30.html

people = 30
cars = 40
trucks = 15

if cars > people :
    print("We shuld take the cars.")
elif cars < people :
    print("We shuld not take the cars.")
else:
    print("We cna't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then."
          )