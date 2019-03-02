""" Инструкция по работе с моим калькулятором:
    1.Для того, чтоб умножить или поделить, прибавить или отнять, Вам нужно в запросе "Введите операцию" вписать +,-,*,/
    2.Чтобы получить Косинус или Синус числа, Вам нужно вписать либо sin либо сos."""
import math
import datetime

print(__doc__)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b
def div(a, b):
    return a / b


def mul(a, b):
    return a * b
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a) 

calc_o = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul,
    'sin':sin,
    'cos':cos
}
 
while True:
    try:
        first_n = float(input('Введите число>>>'))
        oper = input('Введите операцию >>> ')
        if oper != 'sin' and oper != 'cos':
            second_n = float(input('Введите второе число>>>'))
            print(calc_o[oper](first_n, second_n))
        else:
            print(calc_o[oper](first_n))

        
        con = input("you want to continue? y / n?")
        if con == "n":
            break
    except KeyError:

        with open ('log.txt','a') as logfile:
            print('Sorry but my calc dont support operation')
            print('Sorry but my calc dont support operation '+str(datetime.datetime.now()),file = logfile)

    except Exception as e:
        print("try again")
        with open ('log.txt','a') as logfile:
            print(type(e),str(datetime.datetime.now()),file = logfile)
