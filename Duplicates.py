class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if nums[abs(nums[i])]>=0:
                nums[abs(nums[i])]=-nums[abs(arr[i])]
            else:
                print(abs(nums[i]),end='')
