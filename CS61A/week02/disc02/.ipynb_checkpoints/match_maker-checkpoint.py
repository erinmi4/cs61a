"""
实现 match_k，它接受整数 k 并返回一个函数，该函数接受变量 x，如果 x 中相距 k 的所有数字都相同，则返回 True。
例如，match_k(2) 返回一个单参数函数，该函数接受 x 并检查 x 中相距 2 的数字是否相同。 
match_k(2)(1010) 的值为 x = 1010 和从左到右的数字 1, 0, 1, 0。 1 == 1 且 0 == 0，因此 match_k(2)(1010) 结果为 True。 
match_k(2)(2010) 的值为 x = 2010 和从左到右的数字 2, 0, 1, 0。 2 != 1 且 0 == 0，因此 match_k(2)(2010) 结果为 False。
"""

def match_k(k):
    """Returns a function that checks if digits k apart match.
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if x %10 != x % (10 ** k):
                return False
            x //= 10 # 这是一次迭代，去除末位数字 
        return True 
    return check 