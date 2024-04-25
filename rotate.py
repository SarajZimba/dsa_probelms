# def rotate(nums, k):
#     n = len(nums)
#     k = k % n  # To handle cases where k > n
#     if k == 0:
#         return nums

#     def reverse(arr, start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1

#     reverse(nums, 0, n - 1)
#     reverse(nums, 0, k - 1)
#     reverse(nums, k, n - 1)

#     return nums

# # Example usage:
# nums1 = [1, 2, 3, 4, 5, 6, 7]
# k1 = 3
# print(rotate(nums1, k1))  # Output: [5, 6, 7, 1, 2, 3, 4]

# nums2 = [-1, -100, 3, 99]
# k2 = 2
# print(rotate(nums2, k2))  # Output: [3, 99, -1, -100]


class Solution:
    def rotate(self, nums, k):
        n= len(nums)

        k = k % n

        if k ==0 :
            return 0
        
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]

                start += 1
                end -= 1
            
        reverse(nums, 0, n-1)
        reverse(nums, k, n-1)
        reverse(nums, 0, k-1)

        return nums
    
solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6], 3))
        

