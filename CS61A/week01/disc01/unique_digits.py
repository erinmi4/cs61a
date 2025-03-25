def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    # unique 也就是说出现次数 为 1
    i = 0
    num = 0 # unique 数量 
    while i < 9 : 
        has_digit(n,i)
        n = n // 10 

        i += 1 
        

def has_digit(n, k):
    """Returns whether k is a digit in n.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    sel = 0 
    while n != 0 : 
        sel = n % 10 
        n = n // 10 
        if sel ==  k :
            return True
    return False

print(has_digit(10, 1))