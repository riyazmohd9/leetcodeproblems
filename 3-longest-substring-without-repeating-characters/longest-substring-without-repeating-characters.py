class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=maxi = 0
        res = ""
        for i in s:
            if i not in res:
                res += i
                count += 1
                maxi = max(maxi,count)
            elif i == res[-1]:
                maxi = max(maxi,count)
                res = i
                count = 1

            else:
                res  = res[res.index(i)+1:]+i
                count = len(res)
                maxi = max(maxi,count)
        return maxi
       