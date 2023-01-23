# Задача 1
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
number = input('Введите вещественное число: ')
'''
def summa (number):
    summa = 0
    for i in number:
        if i != '.':
            summa = summa + int(i)
    return summa
'''
summa = sum(map(int, number.replace('.', '')))
print (summa)