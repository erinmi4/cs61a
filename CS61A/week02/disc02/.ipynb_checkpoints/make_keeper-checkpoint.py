
"""
实现 make_keeper，它接受一个正整数 n 并返回一个函数 f，该函数将另一个单参数函数 cond 作为其参数。 
当在 cond 上调用 f 时，它会打印出从 1 到 n（包括 n）的整数，其中 cond 在对每个整数调用时返回一个真值。
每个整数都打印在单独的行上。
"""
def is_even(x):
    if x % 2 == 0: 
        return 0 
    return 1 

def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False) # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        i = 1 
        print(i) 
        i += 1 
    return f 

def cond(i) : 
    if i <=  n: 
        return True 
    else : 
        return False