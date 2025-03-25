
"""
python -m doctest digit_finder.py
实现 find_digit，它接受正整数 k 并返回一个函数，该函数接受正整数 x 并返回 x 右侧的第 k 位数字。
如果 x 的位数少于 k，则返回 0。
例如，在数字 4567 中，7 是右起第 1 位数字，6 是右起第 2 位数字，右起第 5 位数字是 0（因为有只有 4 位数字）。
重要提示：您不能使用字符串或索引来解决此问题。尝试仅使用一行来解决此问题。
"""

def find_digit(k):
    """Returns a function that returns the kth digit of x.
    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0  
    "*** YOUR CODE HERE ***"
    return lambda  num :  (num // 10 ** (k-1) ) % 10  

