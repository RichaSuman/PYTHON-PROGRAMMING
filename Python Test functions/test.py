def isPalindrome(x: int) -> bool:
        xtemp = x
        xnew = 0
        if x < 0:
            return False
        
        while xtemp:
            t = xtemp%10
            xnew = xnew*10 + t
            xtemp = xtemp/10
        
        return x == xnew

isPalindrome(10)
isPalindrome(-10)
isPalindrome(121)