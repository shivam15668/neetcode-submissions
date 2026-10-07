class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
         result = []
         path = []

         def backtrack(start, close):
            if start == n and close == n:
                result.append("".join(path))
                return
            
            if start < n:
              path.append("(")
              backtrack(start+1, close)
              path.pop()
          
            if close < start:
              path.append(")")
              backtrack(start, close+1)
              path.pop()
         backtrack(0,0)
         return result