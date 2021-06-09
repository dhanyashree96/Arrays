import numpy as np
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        '''another solution
        mx=a[-1]
        mx2=b[-1]
        ans=0
        if mx>mx2:
            ans=mx
        else:
            ans=mx2
        newtable=[0]*(ans+1)
        #print(a[0],end='')
        newtable[a[0]]+=1
        for i in range(1,n):
            if a[i]!=a[i-1]:
                #print(a[i],end='')
                newtable[a[i]]+=1
        for j in range(0,m):
            if newtable[b[j]]==0:
                #print(b[j],end='')
                newtable[b[j]]+=1
        return len(newtable)'''
        c=np.union1d(a,b)
        return len(c)
