# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1
# Replacing the calculated values gives us the following expression
# 4! = 4 * 3 * 2 * 1
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(3))
#######################
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# The Fibonacci numbers are defined by: Fn = Fn-1 + Fn-2 => with $F_0 = 0$ and $F_1 = 1$
def fibonacci_func(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_func(n-1) + fibonacci_func(n-2)
# print(fibonacci_func(8))
#######################
# Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3
# f(1) = 1 * 3
# f(2) = 2 * 3
# f(n+1) = f(n) * 3 + f(1) * 3
def f_of_n(n):
    if n==1:
        return 3
    else:
        return f_of_n(n-1) + 3
# for i in range(1,5):
#     print(f_of_n(i))
#######################
# Write a recursive Python function that returns the sum of the first n integers. (Hint: The function will be similiar to the factorial function!)
# 5 = 5+4+3+2+1
def sum_of_n(n):
    if n==0:
        return 0
    else:
        return n + sum_of_n(n-1)
# print(sum_of_n(3))
#######################
 #                  1
 #
 #                1    1
 #
 #            1     2     1
 #
 #        1     3     3     1
 #
 #    1     4     6     4     1
 #
 # 1     5     10    10     5    1
def pascal_triangle(n):
    if n==1:
        return [1]
    else:
        line = [1]
        previous_line = pascal_triangle(n-1)
        print(previous_line)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
print(pascal_triangle(3))

# def pascal(n):
#     if n == 1:
#         return [1]
#     else:
#         line = [1]
#         previous_line = pascal(n-1)
#         for i in range(len(previous_line)-1):
#             line.append(previous_line[i] + previous_line[i+1])
#         line += [1]
#     return line
#
# print(pascal(6))
#######################
#######################