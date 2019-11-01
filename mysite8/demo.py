class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        b=len(matrix)-1
        r=len(matrix[0])-1
        t=l=0
        s=len(matrix)*len(matrix[0])
        c=0
        res=[]
        while c<=s:
            for i in range(l,r+1):
                res.append(matrix[t][i])
                c+=1
            t+=1
            if c==s:
                return res
            for i in range(t,b+1):
                res.append(matrix[i][r])
                c+=1
            r-=1
            if c==s:
                return res
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
                c+=1
            b-=1
            if c==s:
                return res
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
                c+=1
            l+=1
            if c==s:
                return res

s=Solution()
print(s.printMatrix([[1]]))