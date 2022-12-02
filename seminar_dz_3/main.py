# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.


hex_sym = {
    0: '0',
    1: '1', 
    2: '2', 
    3: '3', 
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
    }
new_int = int(input("Введите десятичное число: "))
int1 = new_int
hexa = ''

while new_int > 0:
    hexa = hex_sym[new_int % 16] + hexa
    new_int = new_int // 16
if int1 == 0:
    print(f'Число "{new_int}" в шестнадцатиричной сс "{new_int}"')
else:
    print(f'Число {int1} шестнадцатиричной сс "{hexa}"')


# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом.

'''new_int = input("Введите строку: ")

if new_int:
    if new_int == float:
        print(f"{new_int} - является дробным числом")
else:
    print("Вы ввели обычную строку!")'''


# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о". 
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается

'''
o_str = input('Введите строку на русской раскладке: ')
o_low = o_str.lower()

min_index = 0 
max_index = 0

for let_o in range(len(o_low)):
    if o_low[let_o] == "о": # проверка русской "о"
        min_index = let_o
        break
for let_o in range(len(o_low)-1, -1, -1):
    if o_low[let_o] == "о": # проверка русской "о"
        max_index = let_o
        break
if min_index > 0 or max_index > 0:
    o_reverse = (o_low[:min_index] + o_low[max_index:min_index:-1] + o_str[max_index:])
    print(f'Перевернутый промежуток: {o_reverse}')
else:
    print("Буква 'о' отсутствует!")
'''