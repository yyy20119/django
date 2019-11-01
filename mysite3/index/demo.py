# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        dp=[0 for i in range(number+1)]
        dp[1]=1
        for i in range(2,number+1):
            dp[i]=dp[i-2]+2
        return dp[-1]

s=Solution()
print(s.rectCover(4))