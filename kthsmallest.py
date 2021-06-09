import array as arr
class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        a=[]
        for i in range(0,r+1):
            b=arr[i]
            a.append(b)
        return a[k-1]
