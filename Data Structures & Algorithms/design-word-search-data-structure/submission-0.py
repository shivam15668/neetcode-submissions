class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.isWord

            char = word[i]

            if char == "." :
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            
            if char not in node.children:
                return False
            
            return dfs(node.children[char], i+1)
        
        return dfs(self.root,0)
        
