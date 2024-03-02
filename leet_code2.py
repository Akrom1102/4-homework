# PALINDROME

class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            print("manfiy son")
            return False

        else:
            print("musbat son")
            return True


x = int(input("Enter number: "))
sol = Solution()
print(sol.isPalindrome(x))
