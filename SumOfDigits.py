#Sum of Digits of number n

def digital_root(n):
    end = 1
    result = n%10
    loop = (n-n%10)/10
    while loop>=1:
        result = result + loop%10   
        loop = (loop-loop%10)/10
        if loop<1:
            if ((result-(result%10))/10)>0:
                loop = result
                result = 0
            
    return result