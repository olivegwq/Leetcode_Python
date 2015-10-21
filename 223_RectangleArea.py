class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left=max(A,E)
        right=min(C,G)
        top=min(D,H)
        bottom=max(B,F)
        Area=(C-A)*(D-B)+(G-E)*(H-F)
        if right<=left or top<=bottom:
            return Area
        else:
            return Area-(right-left)*(top-bottom)
