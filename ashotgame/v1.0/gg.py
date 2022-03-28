#Guess numbers

###FUNCTIONS
import random

def engine_NumberGen():
    return random.randint(1, 10)
    
def engine_Input_IO():
    return int(input("Введи рандомное число от 1 до 10 >>> "))
    
def engine_Input_Check(user_input, rand_number):
    if user_input == rand_number:
        return True
    else:
        return False

def engine_Output_result(result):
    if result:
        print("АЙ МАЛАЦА! ЧЁТКО!")
    else:
        print("ВАЙ! ТЫ НЕ УГАДАЛ. МНЕ СТЫДНО ЗА ТЕБЯ")

def engine_Main():
    rand_number = engine_NumberGen()
    user_input = engine_Input_IO()
    result = engine_Input_Check(user_input, rand_number)
    engine_Output_result(result)
    
#Run Game
print('Угадалка от Ашота v1.0b3')
engine_Main()

def engine_Loop():
    while True:
        engine_Main()

engine_Loop()