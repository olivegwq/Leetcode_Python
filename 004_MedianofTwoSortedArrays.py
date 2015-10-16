'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count=len(nums1)+len(nums2)
        flag=count%2  #denote whether it is an odd number
        head1,head2,current,i=0,0,0,0
        
        while head1<len(nums1) and head2<len(nums2) and i<count/2:
            if nums1[head1]<nums2[head2]:
                current=nums1[head1]
                head1+=1
                i+=1
            else:
                current=nums2[head2]
                head2+=1
                i+=1
        if i==count/2 and head1<len(nums1) and head2<len(nums2):
            if flag:
                return min(nums1[head1],nums2[head2])
            else:
                return (min(nums1[head1],nums2[head2])+current)/2.0
        elif i==count/2 and head1<len(nums1):
            if flag:
                return nums1[head1]
            else:
                return (nums1[head1]+current)/2.0
        elif i==count/2 and head2<len(nums2):
            if flag:
                return nums2[head2]
            else:
                return (nums2[head2]+current)/2.0
        elif head1==len(nums1):
            head2+=count/2-i
            if flag:
                return nums2[head2]
            else:
                return (nums2[head2]+nums2[head2-1])/2.0
        elif head2==len(nums2):
            head1+=count/2-i
            if flag:
                return nums1[head1]
            else:
                return (nums1[head1]+nums1[head1-1])/2.0
