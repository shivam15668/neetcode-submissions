class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root

            for char in word:
               if char not in node.children:
                node.children[char] = TrieNode()
               node = node.children[char]
            node.word = word

        # dfs

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r,c,node):
            char = board[r][c]

            if char not in node.children:
                return
            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None

            board[r][c] = "#"

            for dr,dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr = r+dr
                nc = c+dc

                if 0<= nr < rows and 0<= nc < cols:
                    dfs(nr,nc, node)
                
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return result
