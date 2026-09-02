
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = {}

        left = 0
        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                windowLen = right - left + 1

                if windowLen < resLen:
                    resLen = windowLen
                    res = [left, right]

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        left, right = res

        return s[left:right + 1] if resLen != float("inf") else ""