class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1,self.s2=[],[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.s1:
            self.s1.append(x)
        else:
            self.s2.append(x)
    

    def pop(self):
        """
        :rtype: nothing
        """
        self.s1.pop()
        
        while len(self.s2)>1:
            self.s1.append(self.s2.pop())
        self.s1,self.s2=self.s2,self.s1

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1
