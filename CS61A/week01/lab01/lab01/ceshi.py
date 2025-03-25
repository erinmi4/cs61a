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
