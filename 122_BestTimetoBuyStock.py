class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        cur=0
        low,total=0,0
        state=0 #no stock
        
        while cur <len(prices)-1:
            if prices[cur+1]<prices[cur] and state:
                total+=prices[cur]-low
                state=0
                cur+=1
                low=prices[cur]
            elif prices[cur+1]<prices[cur] and not state:
                cur+=1
                low=prices[cur]
            elif prices[cur+1]>=prices[cur] and state:
                low=min(low,prices[cur])
                cur+=1
            else:
                low=prices[cur]
                cur+=1
                state=1
        if state:
            total+=prices[-1]-low
        return total
