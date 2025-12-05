from functools import lru_cache

FIVE_NAMES = ["Alice", "Bob", "Charlie", "David", "Eve"]
AGES = [25, 30, 35, 40, 45]
MAP_NAME_TO_AGE = {name: age for name, age in zip(FIVE_NAMES, AGES)}

def average_age():
    return sum(AGES) / len(AGES)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def fibonacci_memoized(n):
    @lru_cache(maxsize=None)
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    return fib(n)

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)    
    
LAST_NAMES = ["Smith", "Johnson", "Williams", "Jones", "Brown"]

def get_last_name(name):
    if name in MAP_NAME_TO_AGE:
        return LAST_NAMES[FIVE_NAMES.index(name)]
    else:
        return None
    
def fib3(n):
    if n <= 0:
        return 0