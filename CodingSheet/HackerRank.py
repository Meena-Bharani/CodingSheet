# https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true
# get rid of pair of adjacent characters
# s = 'aab'  # output b
# s = 'abba'  # output Empty String
# s = 'aaabccddd'  # output abd
# s = 'aa'  # output Empty String
# s = 'baab'  # output Empty String
def superReducedString(s):
    # Write your code here
    result = []
    for i in s:
        if len(result) ==0:
            result.append(i)
        else:
            if result[len(result)-1] == i:
                result.pop(len(result)-1)
            else:
                result.append(i)
    res = ''.join(result)
    if len(result)==0:
        res = 'Empty String'
    return res


# https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true
# s = oneTwoThree  #output = 3
# s = saveChangesInTheEditor  #output = 5

def camelcase(s):
    # Write your code here
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    count +=1
    return count

# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
# All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
# minimum required chars 6
# input
# 3
# Ab1
# output
# 3  # total 6 required
# input
# 11
# #HackerRank
# output
# 1  # number missing
# input
# 6
# meena
# output
# 3  # even though 1 less for 6, 3 will be the ans. capital, number and symbol (totally 3) are missing. get the max value of (3 and 1)

import re
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    min_required = 0
    required_chars = 0
    if n < 6:
        min_required = 6 - n
        print(min_required)
        # return min_required
    # _all = re.search(password,r'[a-zA-Z0-9!@#$%^&*+()-]')
    small = re.search(r'[a-z]', password)
    capital = re.search(r'[A-Z]', password)
    number = re.search(r'[0-9]', password)
    special = re.search(r'[!@#$%^&+*()-]', password)
    if not small:
        required_chars += 1
    if not capital:
        required_chars += 1
    if not number:
        required_chars += 1
    if not special:
        required_chars += 1
    # print(small,capital, number, special ,required_chars)
    result = required_chars if n >= 6 else max(required_chars, min_required)
    return result

# Unexpected Demand
# input
# 2  ## no of orders needed
# 10
# 30
# 40
# output
# 2  ## order = [10,30] with 40. both the orders can be fulfilled
# input
# 3 ## no of orders needed
# 5
# 4
# 6
# 3
# output 0  ## order [5,4,6] with 3. none of the order can be fulfilled.
def filledOrders(order, k):
    # Write your code here
    total = 0
    for i, j in enumerate(sorted(order)):
        if total + j <= k:
            total += j
        else:
            return i
    else:
        return len(order)

# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
# between-two-sets
def getTotalX(a, b):
    # Write your code here
    # multiples of a array and factors of b array
    # multiples a: 2 => 2,4,6,8,10,12,14...
    # multiples a: 6 => 6,12,18,24,30,36...
    # factors b: 24 => 2,3,6,8,12,24
    # factors b: 36 => 2,3,4,6,12,18,36
    # output => common for all 4 => 6,12

    c = 0
    # since the common numbers are lies between 6 and 24, consider those as a start and end points
    for n in range(max(a), min(b) + 1):
        if all(n % x == 0 for x in a):
            if all(x % n == 0 for x in b):
                c += 1
    return c
    # c=0
    # for i in range(max(a), min(b)+1):
    #     af=True
    #     bf=True
    #     for j in a:
    #         if i % j != 0:
    #             af=False
    #             break
    #     if af:
    #         for k in b:
    #             if k % i != 0:
    #                 bf=False
    #     if af and bf:
    #         c+=1
    # return c