from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range (len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except :
            error += 1
    return error

def speed_time(time_s, time_e, userimput):
    time_dalay = time_e - time_s
    time_R = round(time_dalay, 2)
    speed = len(userimput)/ time_R
    return round(speed)
while True:
    ck = input("Ready to test : y/n : ")
    if ck == "y":
        test = ["Typing is an essential skill in the modern world", " It helps us write faster and communicate more effectively The more you practice", "the better your speed and accuracy become", "Always focus on typing without looking at the keyboard"]

        test1 = r.choice(test)
        print("     ****** typing speed ******")
        print(test1)
        print()
        print()

        time_1 = time()
        testinput = input("     Enter : ")
        time_2 = time()

        print('Speed : ', speed_time(time_1, time_2, testinput), " W/ Sec")
        print("Error : ", mistake(test1, testinput))

    elif ck == "n":
        print("Thank you ")
        break
    else:
        print("wrong input")