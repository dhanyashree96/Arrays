class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans=arr[n-1]-arr[0]
        mn,mx=0,0
        for i in range(1,n):
            mn=min(arr[0]+k,arr[i]-k)
            mx=max(arr[i-1]+k,arr[-1]-k)
            result=min(ans,mx-mn)
        return result
