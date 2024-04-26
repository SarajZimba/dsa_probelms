class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize the pointer for placing unique elements
        k = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # place it in the next available position for unique elements
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    
solution = Solution()
print(solution.removeDuplicates([1, 1, 2, 3, 3,5]))