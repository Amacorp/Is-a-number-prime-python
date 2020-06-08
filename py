from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 
    
    
    
    or
    
    
import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
    
    
    
or



from math import sqrt

def is_prime(n):
  return n > 1 and all(n % d for d in xrange(2, int(sqrt(n)) + 1))
  
  
  
  
or




def is_prime(num):
    if num < 4: return num > 1
    if num % 2 == 0 or num % 3 == 0: return False
    for i in range(5, int(num ** 0.5 + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True
    
    
    
    
    
