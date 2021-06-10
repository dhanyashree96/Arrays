class Solution:
    def sort012(self,arr,n):
        # code here
        start = mid = 0
        pivot = 1
        end=n-1
        while mid <= end:
            if arr[mid] < pivot:      
                temp=arr[start]
                arr[start]=arr[mid]
                arr[mid]=temp
                start = start + 1
                mid = mid + 1
            elif arr[mid] > pivot:    
                temp=arr[mid]
                arr[mid]=arr[end]
                arr[end]=temp
                end = end - 1
            else:                   
                mid = mid + 1
