class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign=-1 if (dividend>0 and divisor <0) or (dividend<0 and divisor>0) else 1
        
        res=0
        A,B=abs(dividend),abs(divisor)
        while A>=B:
            n,b=1,B
            while A>=b:
                n<<=1
                b<<=1
            b>>=1
            n>>=1
            A-=b
            res+=n
            if res>=2147483647 and sign==1:
                return 2147483647
            if res>=2147483648 and sign==-1:
                return -2147483648
        return res if sign==1 else -res
