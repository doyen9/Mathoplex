import random
from random import randint, randrange
import operator
import time
import timeit

from time import time
# import speech_recognition as sr
import pyttsx3
number_right = 0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[2].id)

engine.setProperty('rate', 185 )

def speak(audio) :
  engine.say(audio)
  engine.runAndWait()






# window = Tk()
# window.title("MaTh4U")



speak("what math do you want to practice ??")
print("add - addition , sub - subtraction , mul - multipplication , div - division, Type exit to exit at anytime")

response = str(input("what math do u wnna practice - add , sub , mul or div ?? :        "))

if "add" in response:
    speak('your  questions are on  the way')
    print("your addition questions are on  the way....") 
    
    while True:
        no1 = randint(1,50)
        no2 = randint(1,50)
        converted_no1 = str(no1)
        converted_no2 = str(no2)
        sum = no1 + no2 
        #)
        
        
        speak('wht is the answer for' + converted_no1 + '+' + converted_no2 )
        start_time = time()
        print(converted_no1 + '  +  ' + converted_no2)
        ur_ans_st = str((input(f'wht is the ans for {no1} + {no2}??? :    ')))
        
        

        try:
            ur_ans1 = int(ur_ans_st)
            elapsed_time = time() - start_time

            if ur_ans1 == sum:



                print(f'the answer is right!!!')
                speak('that is the right answer !!!')
                number_right += 1
                new_elap = str(round(elapsed_time,1))
                print("Time taken to answer is  " + new_elap + " Seconds")

            else:
                number_right -= 1
                print("nope, ur wrong mate, the right ans was")
                speak("nope, your answer was wrong ")
                print(sum)
            
        except ValueError:
            except ValueError:
            newnumright = str(number_right)
            print(newnumright)
            speak("Your total score is " + newnumright)
            speak("exiting")
            print('exiting')
            break
            
            

        # elif not response:
        #     print("see u next time buds")
        #     break
        
        # elif str_ans == ext:
        #     break

       
        # else:
        #     print("nope, ur wrong mate, the right ans was")
        #     speak("nope, your answer was wrong ")
        #     print(sum)
        
    
if "s" in response:
    while True:
        nom1 = randint(1,100)
        nom2 = randrange(nom1, 100)
        converted_nom1 = str(nom1)
        converted_nom2 = str(nom2)

        
        diff = nom2 - nom1 
         
        speak("what is the difference of " + converted_nom2 + "-" +converted_nom1 )

        start_time2 = time()
        ur_ans2 = str(input(f'what is the diff if {nom2} - {nom1} ?????  :     '))
        
        try:
            ur_ans_nn = int(ur_ans2)
            elapsed_time2 = time() - start_time2

            if ur_ans_nn == diff:
                print("tht is the right answer!")
                speak("that is the right answer")
                number_right += 1
                new_elap2 = str(round(elapsed_time2,1))
                print("Time taken to answer is " + new_elap2 + " seconds" )

            else:
                number_right -= 1
                print("that was the wrong answer")
                speak("It is the wrong answer ")
                print(diff)
        
        except ValueError:
            newnumright = str(number_right)
            print(newnumright)
            speak("Your total score is " + newnumright)
            speak("exiting")
            print('exiting')
            break
        

if "mul" in response:
    while True:

        num1 = randint(2,9)
        num2 = randint(2,9)
        converted_num1 = str(num1)
        converted_num2 = str(num2)
        prod = num1 * num2
        speak("What is the answer for " + converted_num2 + "multiplied by " + converted_num1)
        start_time3 = time()

        ans = str(input(f'what the ans {num1} * {num2}????'))
        
        try:
            anns = int(ans)
            elapsed_time3 = time() - start_time3

            if anns == prod:
                print("ur on the right track buds")
                speak("You are on the right track ")
                number_right += 1
                new_elap3 = str(elapsed_time3,1)
                print("Time taken to answer is " + new_elap3 + "seconds")

            else:
                number_right -= 1
                print("Nah, that was the wrong answer")
                speak("That was the wrong answer again, you dumb")
                print(prod)

        except ValueError:
            newnumright = str(number_right)
            print(newnumright)
            speak("your total score is" + newnumright)
            speak("exiting")
            print("exiting")
            break

                        
if "div" in response:
    while True:
        var1 = randint(1,100)
        var2 = randrange(var1,100)
        conv_var1 = str(var1)
        conv_var2 = str(var2)

        qut = round((var2 / var1),1) 
        start_time4 = time()
        speak("what is " + conv_var2 + "divided by " + conv_var1)
        urans3 = str(input(f'whts the ans mate {var2} / {var1} ?? :   '))

        try:
            urrans3 = int(urans3)
            elapsed_tim = time() - start_time4

            if urrans3 == qut:

                print("your ans is right buds")
                number_right += 1
                speak("That is the right answer")
                new_elap4 = str(round(elapsed_tim,1))
                print("time taken to answer is " + new_elap4 + "seconds")

            else:
                print("that was the wrong answer")
                number_right -= 1
                speak("that was the wrong answer")
                print(qut)
        except ValueError:
            newnumright = str(number_right)
            print(newnumright)
            speak("your total score is" + newnumright)
            print("exiting")
            speak("exiting")



        




        







