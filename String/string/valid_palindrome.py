class Solution(object):
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        flag=0
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            right-=1
            left+=1
        return True
           