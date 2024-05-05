# Характеристки коллекцій:
# - доступні операції (додавання, видалення, куди додавати та де видаляти)
# - способом доступа (пошук, доступ по індексу, доступ по ключу)
# - складністю (complexity) операцій


# List (список) - коллекція куди можна додавати/видаляти в будь яке місце, та звертатися за індексом
x = [1, 33, 56, 2, 18]
x.append(54)
x.remove(<value>) - видалити по значенню
x.pop(<index>) - видалити по індексу, повертає видалений елемент
x.sort() - сортування по зростанню
x.reverse() - розвернути в зворотньому напрямку (без сортування)
len(<список>) - довжина

if (x):
    print('not empty')

List comprehension: - не змінює вихідний список
----------
[el*2 for el in x]

result = []
for el in x:
    result.append(el*2)
---------
[el*2 for el in x if el % 3 == 0]

result = []
for el in x:
    if (el % 3 == 0):
        result.append(el*2)
--------
# Dictionary (словник) - {key,value}, кожен ключ може бути доданий тільки один раз, повторне додавання з існуючим ключем переписує значення
dct = { 'Alice': 34, 'Bob': 27, 'John': 45}

dct[key] = value
dct['Mary'] = 12 - за умови відсутності ключа - кидає помилку і припиняє подальше виконання програми

x = dct['Alice']

dct.get(key)
dct.get('Bob') - значення за замовчанням - None, не кидає помилку якщо такого ключа немає
dct.get('Bob', -1)

dct.update(key, value)
dct.update('Bob', 45)

dct.keys()
dict_keys(['Alice', 'Bob', 'John'])

dct.values()
dict_values([34, 27, 45])

dct.items()
dict_items([('Alice', 34), ('Bob', 27), ('John', 45)])

{v:k for k,v in dct.items()}
{34: 'Alice', 27: 'Bob', 45: 'John'}

{k:2*v for k,v in dct.items()}
{'Alice': 68, 'Bob': 54, 'John': 90}

{k:v for k,v in dct.items() if v < 30}
{'Bob': 27}

lst = ['fruit', 'cat', 'dragonfly']
{el:len(el) for el in lst}
{'fruit': 5, 'cat': 3, 'dragonfly': 9}

# Set (набір) - набір унікальний значень. Кожне значення буде присутнє тільки один раз, навіть якщо додане багато разів.
s = {1, 43, 46, 23, 12, 13, 15, 83}
hash(1)  =  0 - 1
hash(12) = 10 - 12, 13, 15
hash(15) = 10
hash(23) = 20 - 23
hash(43) = 40 - 43, 46
hash(46) = 40

filter = { 1209856823, 77593503825, 359237595, 2395793578 }
# read file

# Операції - https://www.w3schools.com/python/python_sets_methods.asp

# Tuple (кортеж) - статичний набір значень (immutable).
t = (2, 'abs')
t[0]
t[1]