

def Fizzbuzz(n):
    """
• If i is divisible by both 3 and 5, print fizzbuzz.
• If i is divisible by 3 (but not 5), print fizz.
• If i is divisible by 5 (but not 3), print buzz.
• Otherwise, print the number i.
    """
    k = 0  ; 

    while k < n : 
        k += 1  
        if k % 3 == 0  and k % 5 == 0:
            print("fizzbuzz")
        elif k % 3 == 0  :
            print("fizz")
        elif k % 5 == 0  :
            print("buzz")
        else :
            print(k)
            


Fizzbuzz(16)        



