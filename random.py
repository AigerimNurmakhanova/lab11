'''
import random
 
number = random.random()  # значение от 0.0 до 1.0
print(number)
number = random.random() * 100  # значение от 0.0 до 100.0
print(number)
'''

'''
import random
 
number = random.randint(20, 35)  
print(number)
#min мен max арасындағы сандарды шығарып береді
'''

'''
import random
 
number = random.randrange(10)  # значение от 0 до 10 не включая
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
print(number)
number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
print(number)
'''

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)  #shuffle перемешаеть 
print(numbers)  
random_number = random.choice(numbers)  #choice возвращаееть 
print(random_number)
'''
