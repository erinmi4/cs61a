def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.
    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    prvi,last = 0 , 0 
    while x != 0 : 
        last = x % 10 
        previ,x = (x //10) % 10  , x //10  # 特别注意 这里的 previ 如果不对 10 取余，那么就会得到前面的所有数字
        if last < previ :
            return False 
    return True 