import random
from random import randint, randrange
import operator
import time
import timeit
from tkinter import *
import tkinter

window = Tk()
window.title("MaTh4U")




print("add - addition , sub - subtraction , mul - multipplication , div - division")
response = str(input("what math do u wnna practice - add , sub , mul or div ?? :        "))

if "add" in response:
    while True:
        no1 = randint(1,50)
        no2 = randint(1,50)
        sum = no1 + no2 
        print("your addition questions are on  the way....") 
        time.sleep(0.34)
        

        ur_ans = int((input(f'wht is the ans for {no1} + {no2}??? :    ')))

        start = time.time()

        if ur_ans == sum:
            print("yep thts the one")
            # end = time.time()
            # print("time tajen to ans the ques" )
            #print(start - end)
        
        elif not response:
            print("see u next time buds")
            break
    

       
        else:
            print("nope, ur wrong mate, the right ans was")
        
            print(sum)
        
    
if "s" in response:
    while True:
        nom1 = randint(1,50)
        nom2 = randrange(nom1, 50)
        #while nom2 > nom1:
        diff = nom2 - nom1 
        ur_ans2 = float(input(f'what is the diff if {nom2} - {nom1} ?????  :     ')) #str(input(f'what is the diff if {nom2} - {nom1} ?????  :     '))
        
        
        if ur_ans2 == diff:
            print("idhu idhu ans andre")

        elif not response:
            print("see u next time man")
            break

        else:
            print("nope ur ans is wrong buds")
            print(diff)


if "mul" in response:
    while True:

        num1 = randint(2,9)
        num2 = randint(2,9)

        prod = num1 * num2
        ans = int(input(f'what the ans {num1} * {num2}????'))
        score = 0
        if ans == prod:
            print("ur on the right track buds")
            
            #score += 1
            #print("yur score is " )
            #print(score)

        elif not response:
            print("see you next time bro")
            break

        else:
            print("nope ur wrong man, the right ans was")
            print(prod)

if "div" in response:
    while True:
        var1 = randint(1,100)
        var2 = randrange(var1,100)
        
        qut = round((var2 / var1),1) 
        urans3 = float(input(f'whts the ans mate {var2} / {var1} ?? :   '))

        if urans3 == qut:
            print("yeh man, thts right")
            #except ValueError:
            #print("see u soon")
            #break

        

        else:
            print("nah man, ur wrong bro")
            print(qut)

        

window.mainloop()


        







