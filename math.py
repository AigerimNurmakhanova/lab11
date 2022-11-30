''' 
#(exp)
import math
a = 6
b = -8
c = 2.00

print(math.exp(a))
print(math.exp(b))
print(math.exp(c))

ответ: 403.4287934927351
       0.00033546262790251185
	   7.38905609893065
'''

'''
#(log без[base])

import math
print("math.log(10.43):", math.log(10.43))
print("math.log(20):", math.log(20))
print("math.log(math.pi):", math.log(math.pi))

ответ: math.log(10.43): 2.344686269012681
       math.log(20): 2.995732273553991
       math.log(math.pi): 1.1447298858494002

'''

'''
#(log10)

import math
 # Возвращает log10 числа 50
print("log10 числа 50 равен:", math.log10(50))

ответ: log10 числа 50 равен: 1.6989700043360187
'''


'''
#(log2)

import math
 # Возвращает log2 числа 16
print("log2 числа 16 равен:", math.log2(16))

ответ: log2 числа 16 равен: 4.0
'''

'''
import math
 
num = -4.28
a = 14
b = 8
 
num_list = [10, 8.25, 75, 7.04, -86.23, -6.43, 8.4]
x = 1e-4 # Малое значение x
 
print('Число:', num)
print('Округление числа вниз:', math.floor(num))
print('Округление числа вверх:', math.ceil(num))
print('Модуль числа:', math.fabs(num))
print('Наибольший общий делитель a и b: ' + str(math.gcd(a, b)))
print('Сумма элементов списка: ' + str(math.fsum(num_list)))
print('e^x (при использовании функции exp()) равно:', math.exp(x)-1)
print('e^x (при использовании функции expml()) равно:', math.expm1(x))


ответ:
Число: -4.28
Округление числа вниз: -5
Округление числа вверх: -4
Модуль числа: 4.28
Наибольший общий делитель a и b: 2
Сумма элементов списка: 16.029999999999998
e^x (при использовании функции exp()) равно: 0.0001000050001667141
e^x (при использовании функции expml()) равно: 0.00010000500016667084
'''