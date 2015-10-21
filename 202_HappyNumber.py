class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict={}

        while True:
            sum=0
            while n:
                sum+=math.pow(n%10,2)
                n//=10
            if sum==1:
                return True
            elif sum in dict:
                return False
            else:
                dict[sum]=1
                n=sum
