class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        nstr='1'
        for i in range(1,n):
            cur_str=''
            j=0
            while j<len(nstr):
                count=0
                while nstr[j+count]==nstr[j]:
                    count+=1
                    if j+count==len(nstr):
                        break
                cur_str=cur_str+str(count)+nstr[j]
                j+=count
            nstr=cur_str
            i+=1
        return nstr
