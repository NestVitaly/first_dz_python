# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
list_num = [2, 3, 5, 9, 3, 13, 21, 17, 24, 86]
print(f'Дан список: {list_num}')
list_sum = 0

for i in range(len(list_num)):
    list_index = i
    if list_index % 2 != 0:
        list_sum += list_num[i]

print(f'Суммам элементов стоящих на нечетных позициях: {list_sum}')
'''

# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)



# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

'''
from random import randint as rdt

list_rnd = []

for i in range(30):
    list_rnd.append(rdt(0, 100))
print(f'Сгенерированный список: {list_rnd}')

for i in range(len(list_rnd)-1):
    min_el = list_rnd[i]
    min_index = i
    for j in range(i + 1, len(list_rnd)):
        if min_el > list_rnd[j]:
            min_el = list_rnd[j]
            min_index = j
    if min_index != i:
        temp = list_rnd[i]
        list_rnd[i] = list_rnd[min_index]
        list_rnd[min_index] = temp
print(f'Отсортированный список: {list_rnd}')
'''