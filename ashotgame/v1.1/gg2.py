#Guess numbers

###FUNCTIONS
import random
###FUNCTIONS

#Simple number generator that generates random number at 1 to 10
def engine_NumberGen():
    return random.randint(1, 10)

#Input a number
def engine_Input_IO():
    x = int(input("Введи рандомное число от 1 до 10 >>> "))
    return x

#Checks Input
#If Number, written bu user, equals generated number, then returns true.    
def engine_Input_Check(user_input, rand_number):
    if user_input == rand_number:
        return True
    else:
        return False

#Outputs a result
def engine_Output_result(result):
    if result:
        print("АЙ МАЛАЦА! ЧЁТКО!")
    else:
        print("ВАЙ! ТЫ НЕ УГАДАЛ. МНЕ СТЫДНО ЗА ТЕБЯ")
        
#Core of this game
def engine_Main():
    rand_number = engine_NumberGen()                        #Calls Number generator
    user_input = engine_Input_IO()                          #Calls Input function
    if user_input < 0 or user_input > 10:
        print("Ты идиот? От 1 до 10")
    else:
        result = engine_Input_Check(user_input, rand_number)    #Calls Result Checker
        engine_Output_result(result)                            #Calls Engine output
    
#Run Game
print('Угадалка от Ашота v1.1')
engine_Main()

#Simple engine loop
def engine_Loop():
    while True:
        engine_Main()

#Calls engine loop
engine_Loop()
