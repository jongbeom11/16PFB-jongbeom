#-*-coding:utf8
#http://learnpythonthehardway.org/book/ex31.html

if "raw_input" not in dir(__builtins__):
    raw_input = input

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"
door = raw_input("> ")
#상수를 왼쪽에 두는 것을 권장함 변수는 오른쪽!
if "1" == door:
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if "1" == bear:
        print "The bear eats your face off.  Good job!"
    elif "2" == bear:
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif "2" == door:
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if "1" == insanity or "2" == insanity:
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
