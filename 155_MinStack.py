class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack=[]
        self.stack=[]
      

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack.pop()==self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
