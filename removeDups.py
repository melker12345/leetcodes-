List = [1,1,2,3,1,1]

class Solution:
    def removeDuplicates(self, nums) -> int:

        if not nums:
            return 0  # Handle empty list

        k = 0  # Slow pointer

        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1  # Number of unique elements

        k = removeDuplicates(nums)
        return k, nums[:k]




