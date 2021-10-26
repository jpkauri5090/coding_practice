import time

class Solution:
    def minSubArrayLen(self, nums, s):
        biggest = self.__findBiggest(nums)
        for i in range(len(nums)):
            for k in range(len(nums)):
                if biggest + nums[k] >= s:
                    return k + 1
            
            return 0
      
        
    def __findBiggest(self, nums):
        biggest = 0
        for i in range(len(nums)):
          if nums[i] >= biggest:
              biggest = nums[i];
    
        return biggest
start = time.time()
print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)

end = time.time()

print( "time : ", end - start)
  
# class Solution(object):
#   def minSubArray(self, k, nums):
#     leftIndex = rightIndex = 0
#     sum = 0
#     minLen = float('inf')

#     while rightIndex < len(nums):
#       sum += nums[rightIndex]
#       while sum >= k:
#         minLen = min(minLen, rightIndex - leftIndex + 1)
#         sum -= nums[leftIndex]
#         leftIndex += 1
#       rightIndex += 1

#     if minLen == float('inf'):
#       return 0
#     return minLen

# start = time.time()
# print Solution().minSubArray(7, [2, 3, 1, 2, 4, 3])

# end = time.time()

# print( "time : ", end - start)