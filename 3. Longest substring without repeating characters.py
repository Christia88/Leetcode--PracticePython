class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1=""
        str2=""
        l=len(s)
        for i in range(0,l):
            for j in range(i,l):
                if s[j] not in str2:
                    str2+=s[j]
                else:
                    if len(str2)>len(str1):
                        str1=str2
                    str2=""
                    break
        if len(str2)>len(str1):
            str1=str2
        return len(str1)
