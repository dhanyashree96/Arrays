class Solution:
	def minJumps(self, arr, n):
	   end=0
	   jumps=0
	   farthest=0
	   for i in range(n-1):
	        farthest=max(farthest,i+arr[i])
	        if i==end:
	            jumps+=1
	            end=farthest
	   return jumps
