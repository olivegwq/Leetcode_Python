class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return 0
        
        head, tail,vol=0,len(height)-1,0
        
        while head<tail:
            vol=max(vol,min(height[head],height[tail])*(tail-head))
            if height[head]<=height[tail]:
                head+=1
            else:
                tail-=1
            
        return vol
