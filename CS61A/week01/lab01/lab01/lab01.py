def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k  == 0 :
        return 1 
    i = 0
    result = 1 
    while i < k : 
        result *= n 
        n = n - 1 
        i = i + 1 
    return result 

def divisible_by_k(n, k):
    """
    Write a function divisible_by_k that takes positive integers n and k. 
    It prints all positive integers less than or equal to n that are divisible by k from smallest to largest. 
    Then, it returns how many numbers were printed.

    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    # 设定一个数 mk , 因为相除 ，也就是看 k , 2k , 3k ..... mk  是否小于 n 
    mk = k 
    i = 0 
    while  mk <= n : 
         print(mk)
         mk = mk + k
         i += 1 
    return i   

def sum_digits(y):
    """Sum all the digits of y.
    Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # 获取每一个digits , 然后将其逐个相加 , 相加 time次数 ，time是位数 
    i = 0 
    while y  != 0  :
        i += y % 10 
        y = y // 10 
    return i 
    





def double_eights(n):
    """Return true if n has two eights in a row.
    Write a function that takes in a number and determines if the digits contain two adjacent 8s.

    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # 因为是找到 88
    i = 0 
    j = 0 
    while n != 0 :
        if (n%10) == 8 :
            i+=1 
        else :
            i = 0 
        
        if i == 2 : 
            j = 1 
        elif i > 2 : 
            j = 0 
        n = n // 10 
    
    if j == 1  : 
        return True
    else : 
        return False 
