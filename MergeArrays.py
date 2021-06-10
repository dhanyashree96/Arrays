class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        for i in range(n):
            if arr1[i]>arr2[0]:
                arr1[i],arr2[0]=arr2[0],arr1[i]
            for j in range(m):
                if j+1<m and arr2[j]>arr2[j+1]:
                    arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
                    j=j+1
        return arr1,arr2
