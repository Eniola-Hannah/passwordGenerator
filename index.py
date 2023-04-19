import numpy
import string
import random
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
    user2 = input("""
        How many letter password do you want:
            - 4
            - 6
            - 8
            - 10
                  - """)
    if user2 == "4":
        e = ''.join(random.choices(string.ascii_letters, k=4))
        print("here you go-- " + str(e))
    elif user2 == "6":
        f = ''.join(random.choices(string.ascii_letters, k=6))
        print("here you go-- " + str(f))
    elif user2 == "8":
        g = ''.join(random.choices(string.ascii_letters, k=8))
        print("here you go-- " + str(g))
    elif user2 == "10":
        h = ''.join(random.choices(string.ascii_letters, k=10))
        print("here you go-- " + str(h))
elif user == "3":
    user3 = input("""
        How many digit do you want:
            - 4
            - 6
            - 8
            - 10
                  - """)
    if user3 == "4":
        i = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        print("here you go-- " + str(i))
    elif user3 == "6":
        j = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print("here you go-- " + str(j))
    elif user3 == "8":
        k = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print("here you go-- " + str(k))
    elif user3 == "10":
        l = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print("here you go-- " + str(l))
elif user == "0":
    sys.exit()