class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        count = 1  # Counter for keeping track of repeated elements
        j = 1  # Pointer for placing elements satisfying the condition
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j, nums
    

solution = Solution()
print(solution.removeDuplicates([1, 1, 1,1 ,1, 2, 2,2, 2, 3, 4, 5]))