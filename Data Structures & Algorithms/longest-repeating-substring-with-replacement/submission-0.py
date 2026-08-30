class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count = {} # of all charater
        max_freq = 0 # frequency of highest character
        result = 0 # length of longest valid window

        for right in range (len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left +1 ) - max_freq > k : 
                 count[s[left]] -= 1
                 left += 1

            result = max(result, right-left+1)
        return result