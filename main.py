Одиниці інформації

Bit  - 0 або 1
Byte - 8 біт (01010101)
Kib   - 2*10 bytes = 1024 bytes
Mib   - 2*10 Kb = 1024 Kilobyte
Gib   - 1024 Mb
....

Kb - 1000 bytes
Mb - 1000 Kb
....

2*32
# змінна - variable
# ячейка пам'яті певного розміру в якій зберігаються дані - числа, логічні вирази (True | False), текст, бінарні дані
# - адреса в пам'яті де починається змінна
# - довжина змінної (кількість байт)
# - спосіб считування чи інтерпретації даних

# ================================================
# константа - constants
# змінна яка має стале значення
# використовується щоб дати ім'я певному значенню, спростивши читання та зміну програми
COLOR_RED = 1
COLOR_BLUE = 8
COLOR_GREEN = 16

BICYCLE_TIRE_TYPE_A = 1
BICYCLE_TIRE_TYPE_B = 8

x = COLOR_RED
print(COLOR_RED)
send_network(COLOR_RED)

# ================================================
# оператор - operator (перелічені в порядку приоритетів)
присвоювання значення - =
порівняння - ==, !=, <, =<, >, >=
арифметичні оператори - +,*,-,/,^,%
логічні оператори (boolean) - and, or, not

day_of_week = SATURDAY
month = JANUARY

if (month < MAY and day_of_week == FRIDAY):
    # play chess
    pass

if (day_of_week == MONDAY or day_of_week == THURSDAY):
    # drink coffee
    pass

if (not day_of_week == SUNDAY):
    # wake up early
    pass

AND
X   Y   =
---------
0   0   0
0   1   0 
1   0   0
1   1   1

OR
X   Y   =
---------
0   0   0
0   1   1 
1   0   1
1   1   1

NOT
X  =
----
0  1
1  0


# ================================================
# умовний вираз - 
# 1) if-then-else / conditional statements
if (x == 2):
    # then do this
elif (x > 5 and x < 8):
    # do something
else:
    # alternative
# -------------------------------

# 2) match statement
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")



# цикл - loop
# 1) for (x in <list>):
l = ['a', 23, 'bcd']
for x in l:
    print(x)

for x in 'abcdef':
    print(x)

for x in range(0,5):
    print(str(x) + ') Hello Python')

for x in range(0,5):
    if (x % 2 == 0):
        continue

    print(str(x) + ') Hello Python')

# 2) while loops 
i = 1
while i < 6:
  print(i)
  i += 1

while True:
    is_finished = database.is_operation_completed(id='ab235df') # True or False
    if (is_finished):
        break
    
    print('working....')
    os.sleep(300)

# функція - function
# бібліотека - library

# класс - class
# об'єкт - object 