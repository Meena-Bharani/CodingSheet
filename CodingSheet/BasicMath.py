# find even or odd
def findEvenOdd(n):
    try:
        n = int(n)
        if n%2 ==0:
            print(f'{n} is a Even number')
        elif n%2 !=0:
            print(f'{n} is a Odd number')
    except Exception as e:
        raise Exception('Error! ',e)

# find last digit in a number
def findLastDigitinNumber(n):
    try:
        n = int(n)
        l= list(str(n))
        last = l[len(l)-1]
        print(f'Last digit of {n} is',last)
    except Exception as e:
        raise Exception('Error! ',e)

# count digits in a number  (solving above last digit prob will make this easy for you)
def countDigit(n):
    try:
        n =int(n)
        print(len(str(n)))
    except Exception as e:
        raise Exception('Error! ',e)

# reverse a number (try thinking how youcan use above logic in solving this)
def reverseNumber(n):
    try:
        n = int(n)
        s=''
        for i in str(n):
            s = i+s
        print(f'Reverse of {n} is', int(s))
    except Exception as e:
        raise Exception('Error! ',e)

# find power of a number
def findPower(n,p):
    try:
        n,p=int(n),int(p)
        print(f'Power of {n} is',n**p)
    except Exception as e:
        raise Exception('Error! ',e)

# # GCD
def findGCD(n,m):
    try:
        n = int(n)
        m = int(m)

        # find divisors for n and m
        def divisors(x):
            l = list(filter(lambda i:x % i==0, list(range(1,x))))
            mx = max(l)
            return mx
        
        n_max_divisor = divisors(n)
        m_max_divisor = divisors(m)

        if n_max_divisor == m_max_divisor:
            print(f'GCD of {n} and {m} is {n_max_divisor}')
            return
        print('None')
        return
    except Exception as e:
        raise Exception('Error! ',e)

# print all divisors of a number
def findDivisor(n):
    try:
        n = int(n)
        l =[1]
        for i in range(2,n+1):
            if n%i==0: l.append(i)
        print(f'Divisors of {n} are ',l)
    except Exception as e:
        raise Exception('Error! ',e)

# prime number ((try solving by yourself)
def isPrime(n):
    try:
        n=int(n)
        if n==0 or n==1 or n==2:
            print('{n} is a Prime number')
            return
        else:
            for i in range(2,n-1):
                if n%i==0: 
                    print(f'{n} is not a Prime number')
                    return
        print('Prime')
        return
    except Exception as e:
        raise Exception('Error! ',e)

# amstrong number (solving power of number, will make this easy for you)
def findAmstrongNumber(n):
    try:
        n = int(n)
        tot =0
        l = len(str(n))
        for i in str(n):
            tot += int(i)**l
        if int(n)==int(tot):
            print(f'{n} is a Amstrong number')
        else:
            print(f'{n} is not a Amstrong number')
    except Exception as e:
        raise Exception('Error! ',e)

# check palindrome of number (use the techniques you learnt so far solving above probs and solve this by yourself)
def palindrome(n):
    try:
        n = int(n)
        m = str(n)[::-1]
        if str(m)==str(n):
            print('Palindrome')
        else:
            print('Not Palindrome')
    except Exception as e:
        raise Exception('Error! ',e)

# # square root of a number (try to first figureout algo to solve this)
def squareRoot(n):
    try:
        n = int(n)
        m = n**.5
        print(f'square root of {n} is ',round(m,2))
    except Exception as e:
        raise Exception('Error! ',e)

# # perfect number
import functools
def perfectNumber(n):
    try:
        n = int(n)
        r = []
        for i in range(1,n):
            if n%i==0:
                r.append(i)
        x = functools.reduce(lambda a,b:a+b,r)
        if x==n:
            print(f'{n} is a Perfect number')
            return
        print(f'{n} is not a Perfect number')
        return
    except Exception as e:
        raise Exception('Error! ',e)

if __name__=='__main__':
    n = input('Enter number: ')
    # findEvenOdd(n)
    # findLastDigitinNumber(n)
    # countDigit(n)
    # reverseNumber(n)
    # p = input('Enter number: ')
    # findPower(n,p)
    # m = input('Enter number: ')
    # findGCD(n,m)
    # findDivisor(n)
    # isPrime(n)
    # findAmstrongNumber(n)
    # palindrome(n)
    # squareRoot(n)
    # perfectNumber(n)
    