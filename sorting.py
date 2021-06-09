class Solution:
    def sort012(self,arr,n):
        # code here
        d=[]
        for j in range(0,n-1):
            for i in range(0,n-1):
                if arr[i]>=arr[i+1]:
                    temp=arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1]=temp
                elif arr[i]==arr[i+1]:
                    arr[i]=arr[i+1]
        return arr[j]
