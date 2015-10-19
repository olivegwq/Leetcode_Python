class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #first check rows and columns 
        DictBlk={}
        DictRow={}
        DictCol={}
        for i in range(9):
            DictRow={}
            if i%3==0:
                DictBlk={}
            for j in range(9):
                if not j in DictCol:
                    DictCol[j]={}
                if not j/3 in DictBlk:
                    DictBlk[j/3]={}
                if board[i][j] =='.':
                    continue
                elif board[i][j] in DictRow or board[i][j] in DictCol[j] or board[i][j] in DictBlk[j/3]:
                    return False
                else:
                    DictRow[board[i][j]]=1
                    DictCol[j][board[i][j]]=1
                    DictBlk[j/3][board[i][j]]=1
        return True
