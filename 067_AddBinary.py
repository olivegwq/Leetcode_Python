class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        elif not b:
            return a
            
        A,B=0,0
        for i in range(len(a)):
            an=1 if a[i]=='1' else 0
            A=A*2+an
        for j in range(len(b)):
            bn=1 if b[j]=='1' else 0
            B=B*2+bn
        C=A+B
        c=''
        while True:
            c=str(C%2)+c
            C/=2
            if not C:
                break
        
        return c
