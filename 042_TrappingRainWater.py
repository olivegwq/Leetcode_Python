class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        
        anchor=height.index(max(height))
        
        #left
        indx1,cur_h,vol_left=0,0,0

        while indx1<anchor:
            cur_h=max(cur_h,height[indx1])
            vol_left+=(cur_h-height[indx1])*1
            indx1+=1
        #right
        indx2,cur_h,vol_right=len(height)-1,0,0
        while indx2>anchor:
            cur_h=max(cur_h,height[indx2])
            vol_right+=(cur_h-height[indx2])*1
            indx2-=1
        return vol_left+vol_right
