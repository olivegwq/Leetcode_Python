class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev=[]
        for i in range(rowIndex+1):
            cur=[]
            for j in range(i+1):
                if j==0 or j==i:
                    cur.append(1)
                else:
                    cur.append(prev[j-1]+prev[j])
            prev=cur
            
        return prev
