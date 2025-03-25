def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 1 
    if n<= 1 :
        print("False")
        return

    while i < (n / 2) : 
        i += 1
        if n % i  == 0 : 
            print("False")
            return
    print("True")




#演示时间：用一句话描述您解决 is_prime 问题所实现的过程，您认为无需查看您的代码，人们就可以理解该过程。向小组展示您的解决方案/向全班展示您小组的解决方案。
# 我们有一个数 9 ， 那么我们设定  i = 2  ， 从 2 开始 ， 与2 相除 ，如果为 0  。 说明能被其他数整除。  ， 然后 i 每次加1 ， 直到  n 大小的一半(小一些)， 因为如果大于一半还能相除，则另一个数必然小于1 . 