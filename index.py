import numpy
import sys
import time

user = input("""
    Welcome, So here I have a program that geerate random password:
    here are my options;
        1. All numbers
        2. All letters
        3. Mixture
        0. exit
    - """)

if user == "1":
    user1 = input("""
        How many digit password do you want:
            - 4
            - 6
            - 8
            - 10
                  - """)
    if user1 == "4":
        a = int(numpy.random.random()*10000)
        print("here you go -- " + str(a))
    elif user1 == "6":
        b = int(numpy.random.random()*1000000)
        print("here you go -- " + str(b))
    elif user1 == "8":
        c = int(numpy.random.random()*100000000)
        print("here you go -- " + str(c))
    elif user1 == "10":
        d = int(numpy.random.random()*10000000000)
        print("here you go -- " + str(d))
elif user == "2":
    pass
elif user == "3":
    pass
elif user == "0":
    sys.exit()