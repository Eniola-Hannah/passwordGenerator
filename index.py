import numpy
import string
import random
import sys
import time

user = input("""
    Welcome, So here I have a program that generate random password:
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
            - exit
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
    elif user1 == "exit":
        print("Thanks for using this program")
        sys.exit()
    else:
        print("Input does not match any of the options, try again!!!")
        
elif user == "2":
    user2 = input("""
            1. LowerCase Format
            2. UpperCase Format
            3. exit
                  """)
    if user2 == "1":
        user3 = input("""
            How many letter password do you want:
                - 4
                - 6
                - 8
                - 10
                - exit
                    - """)
        if user3 == "4":
            e = ''.join(random.choices(string.ascii_lowercase, k=4))
            print("here you go-- " + str(e))
        elif user3 == "6":
            f = ''.join(random.choices(string.ascii_lowercase, k=6))
            print("here you go-- " + str(f))
        elif user3 == "8":
            g = ''.join(random.choices(string.ascii_lowercase, k=8))
            print("here you go-- " + str(g))
        elif user3 == "10":
            h = ''.join(random.choices(string.ascii_lowercase, k=10))
            print("here you go-- " + str(h))
        elif user3 == "exit":
            print("Thanks for using this program")
            sys.exit()
        else:
            print("Input does not match any of the options, try again!!!")
    elif user2 == "2":
        user4 = input("""
            How many letter password do you want:
                - 4
                - 6
                - 8
                - 10
                - exit
                    - """)
        if user4 == "4":
            i = ''.join(random.choices(string.ascii_uppercase, k=4))
            print("here you go-- " + str(i))
        elif user4 == "6":
            j = ''.join(random.choices(string.ascii_uppercase, k=6))
            print("here you go-- " + str(j))
        elif user4 == "8":
            k = ''.join(random.choices(string.ascii_uppercase, k=8))
            print("here you go-- " + str(k))
        elif user4 == "10":
            l = ''.join(random.choices(string.ascii_uppercase, k=10))
            print("here you go-- " + str(l))
        elif user4 == "exit":
            print("Thanks for using this program")
            sys.exit()
        else:
            print("Input does not match any of the options, try again!!!")
    elif user3 == "3":
        print("Thanks for using this program")
        sys.exit()
    else:
        print("Input does not match any of the options, try again!!!")
        
elif user == "3":
    user5 = input("""
        How many digit do you want:
            - 4
            - 6
            - 8
            - 10
            - exit
                  - """)
    if user5 == "4":
        m = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        print("here you go-- " + str(m))
    elif user5 == "6":
        n = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        print("here you go-- " + str(n))
    elif user5 == "8":
        o = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        print("here you go-- " + str(o))
    elif user5 == "10":
        p = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        print("here you go-- " + str(p))
    elif user5 == "exit":
        print("Thanks for using this program")
        sys.exit()
    else:
        print("Input does not match any of the options, try again!!!")
elif user == "0":
    print("Thanks for using this program")
    sys.exit()
else:
    print("Input does not match any of the options, try again!!!")