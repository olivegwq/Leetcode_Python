class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        PS=[]
        for i in range(numRows):
            cur=[]
            for j in range(i+1):
                if j==0 or j==i:
                    cur.append(1)
                else:
                    cur.append(PS[i-1][j-1]+PS[i-1][j])
            PS.append(cur)
        return PS
