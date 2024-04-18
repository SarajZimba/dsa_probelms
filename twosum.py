class Solution(object):
    def twoSum(self, nums, target):
        complements = {}
        # print(f"The target is {target}")
        for i, num in enumerate(nums):
            # print([i, num])
            complement = target - num

            # print(i, complement)
            if complement not in complements:
                # print(complement)
                complements[num] = i
            else:
                print([complements[complement], i])
                break

        # print(complements)



solution = Solution()
solution.twoSum([2, 5, 6], 7)

