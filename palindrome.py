class Solution(object):

    def check_palindrome(self, num):
        rev = 0
        prev_num = num
        while(num > 0):        
            moded = num % 10 
            rev = rev * 10 + moded
            num = int(num / 10)
            # print(rev)
        print(rev)

        if prev_num == rev:
            print("True")
        else:
            print("False")

solution = Solution()
solution.check_palindrome(121)




