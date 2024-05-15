# рекурсія це коли функція викликає саме себе
# яка може бути мета - передати результати обчислень отримані 
# на попередньому кроці необхідні як вхідні дані для наступного

# числа Фібоначчі
# 0, 1, 1, 2, 3, 5, 7, 13

# def fib_numbers(numbers_count, numbers=None):
#     if not numbers:
#         return fib_numbers(numbers_count, [0, 1])
    
#     numbers()

#     return result

# print(fib_numbers(1))

# факторіал
# n! (3! 5! 13!)
# 5! = 1*2*3*4*5
# 13! = 1*2*3*4*5*6*7*8*9*10*11*12*13

# 3! = 1*2*3
# abc
# acb
# bca
# bac
# cba
# cab

def factorial(base):
    if (base == 1):
        return 1

    result = base*factorial(base - 1)
    return result

def factorial_no_rec(base):
    result = 1
    for cn in range(1, base+1):
        result = result * cn
    
    return result

# def recursion_no_limit(current = 1):
#     try:
#         result = recursion_no_limit(current + 1)
#         return result
#     except BaseException as ex:
#         print(ex)
#         print("Curren value - " + str(current))

# recursion_no_limit();

n = 6
print(f"Factorial (no recursion) of {n} = {factorial_no_rec(n)}\n")
print(f"Factorial of {n} = {factorial(n)}")