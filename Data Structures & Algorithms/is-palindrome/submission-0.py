class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers: from left and right
        left = 0
        right = len(s) - 1

        #check if it's alphanumeric, yes then compare, no then move forward
        while right > left:
            while not s[right].isalnum() and right > left:
                right -= 1
            while not s[left].isalnum() and right >left:
                left += 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True