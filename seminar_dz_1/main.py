# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


'''
num = int(input('Введите число: '))

if num == 6 or num == 7:
    print(f'{num} -> да')
elif num in range(1, 5):
    print(f'{num} -> нет')
else:
    print(f'Нужно было вводить любое число от 1 до 7!')
'''


# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

'''
result = True

for n in range(0, 8):
    num = bin(n)
    num = num.replace('b', '0')
    X = int(num[-3])
    Y = int(num[-2])
    Z = int(num[-1])
    result = result and (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))

print(result)
'''

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

'''
x = int(input('Введите значение координаты х: '))
y = int(input('Введите значение координаты у: '))

if x == 0 and y == 0:
    print(f'Координаты "x" и "y" не могут быть равны 0!')
elif x > 0 and y > 0:
    print(f'Координаты "x = {x}" и "y = {y}" находятся в первой четверти')
elif x < 0 and y > 0:
    print(f'Координаты "x = {x}" и "y = {y}" находятся во второй четверти')
elif x < 0 and y < 0:
    print(f'Координаты "x = {x}" и "y = {y}" находятся в третьей четверти')
else:
    print(f'Координаты "x = {x}" и "y = {y}" находятся в четвертой четверти')
'''

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

'''
num = int(input('Укажите номер четверти: '))

if num == 1:
    print(f'Диапазон координат в {num} четверти: (x = 1...100; y = 1...100)')
elif num == 2:
    print(f'Диапазон координат во {num} четверти: (x = -100...-1; y = 1...100)')
elif num == 3:
    print(f'Диапазон координат в {num} четверти: (x = -100...-1; y = -100...-1)')
elif num == 4:
    print(f'Диапазон координат в {num} четверти: (x = 1...100; y = -100...-1)')
else:
    print('Нужно было вводить 1, 2, 3 или 4!')
'''

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

'''
x1 = int(input('Введите значение координаты х1: '))
y1 = int(input('Введите значение координаты y1: '))
x2 = int(input('Введите значение координаты х2: '))
y2 = int(input('Введите значение координаты y2: '))

x = (x2 - x1) ** 2
y = (y2 - y1) ** 2

distance = round(((x + y) ** (0.5)), 2)

print(f'A ({x1}, {y1}); B ({x2}, {y2}) -> {distance}')
'''