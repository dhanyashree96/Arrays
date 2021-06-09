class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        mxfar = a[0]
        mx_endinghere = 0
     
        for i in range(0, size):
            mx_endinghere = mx_endinghere + a[i]
            if mx_endinghere < 0:
                mx_endinghere = 0
             
            # Do not compare for all elements. Compare only  
            # when  max_ending_here > 0
            elif (mxfar < mx_endinghere):
                mxfar = mx_endinghere
                 
        return mxfar
