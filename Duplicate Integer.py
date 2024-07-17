##Sorting Solution O(nlogn)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for n in range(len(nums) - 1):
            if nums[n] == nums[n+1]:
                return True
                
        return False
##HashSet Solution O(n) Consumption in memory much higher
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False