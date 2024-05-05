import random

# Область видимості змінних / Variables scope

# def add(a):
#     c = 888
#     return a+x

# # Global Scope
# x = 2
# y = x + 3

# print(add(y))
# print(c) # очікуємо помилку через то що змінна визначена в недоступній області видимості

# if x > 1:
#     b = 100
#     x = 3

# print(b)

# for v in range(0, 10):
#     print(b)
#     print(v)

# 2.2 Функцї / Functions
# 2.3 Callback
# 2.4 Параметри функцій / Arguments- передача значення (by value) та передача посилання (by reference)
def get_odd_elements(lst):
    if not lst:
        return []
    
    return [int(x) for x in lst if int(x) % 2 != 0]


def get_even_elements(lst):
    if not lst:
        return []
    
    return [int(x) for x in lst if int(x) % 2 == 0]

def get_base3_elements(lst):
    if not lst:
        return []
    
    return [int(x) for x in lst if int(x) % 3 == 0]

def build_and_filter(n, filter):
    # generate list of <n> random numbers
    num = [random.randint(1, 100) for _ in range(0, n)]

    # filter them using callback
    return filter(num)
    
def find_first_in_text(txt, criteria):
    if not txt:
        return None
    
    # ch - character
    for ch in txt:
        if criteria(ch):
            return ch
        
    return None

print(get_odd_elements([1, 2, 3]))
print(get_odd_elements([101, 205, 23, 98]))

print(get_odd_elements(['11', '22', '33']))

print('Odd: ' + str(build_and_filter(10, get_odd_elements)))
print('Even: ' + str(build_and_filter(20, get_even_elements)))
print('Base3: ' + str(build_and_filter(23, get_base3_elements)))

print('Custom lambda: ' + str(build_and_filter(23, lambda lst: [x for x in lst if x % 5 == 0])))

input_text = 'toDay my 43 Birthday'
print('Capital letter: ' + find_first_in_text(input_text, lambda b: b.upper() == b))
print('Number: ' + find_first_in_text(input_text, lambda a: a in '0123456789'))

# передача параметра по значенню - pass by value
def change_value(bbb):
    bbb = bbb * 2
    return bbb

x = 100

y = change_value(x)

print('x:' + str(x))
print('y:' + str(y))

# передача по посиланню - pass by reference
def add_el(lst):
    rnd = random.randint(1,100)
    lst.append(rnd)

def immutable_sort(lst):
    result = [x for x in lst]
    result.sort()
    return result

aaa = []
print('List before changes: ' + str(aaa))
add_el(aaa)
add_el(aaa)
add_el(aaa)
print('List after changes: ' + str(aaa))
bbb = immutable_sort(aaa)
print('List aaa after sort: ' + str(aaa))
print('List bbb after sort: ' + str(bbb))