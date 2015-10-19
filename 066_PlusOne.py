class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not len(digits):
            return 0
        flag=1
        result=[]
        for i in range(len(digits)-1,-1,-1):
            result.insert(0,(digits[i]+flag)%10)
            flag=(digits[i]+flag)/10
        if flag:
            result.insert(0,flag)
        
        return result
