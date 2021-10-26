
# def find_continuous_k(list, k):
#   for start in range(len(list)):
#     sum = 0
#     for end in range(start, s
#       sum += list[end]
#       if sum == k:
#         return list[start:end + 1]
#   return None

#Not working for other numbers like 15
def find_continuous_k(list, k):
  previous_sums = {0: -1}
  sum = 0
  for index, n in enumerate(list):
    sum += n
    previous_sums[sum] = index
    if previous_sums.get(sum - k):
      return list[previous_sums[sum-k] + 1: index + 1]
    # print(previous_sums)
  return None




print find_continuous_k([1, 3, 2, 5, 7, 2], 15)


# class Solution(object):
#     def __init__(self, arr):
#         self.arr = arr

#     def __find_modulo_list(givenList, k):
#         return [x for x in givenList if k % x == 0], [x for x in givenList if k % x != 0] 

#     def find_continuous_k(givenList, k):
#         match, nonMatch = self.__find_modulo_list(givenList, k)

#         if(sum(match) == k):
#             return match
#         if(sum(match) > k):
#             return True
#         if(sum(match) < k):
#             return True
