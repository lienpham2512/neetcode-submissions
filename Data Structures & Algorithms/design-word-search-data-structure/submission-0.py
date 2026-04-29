class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            #base case:
            if index == len(word):
                return "#" in node
            ch = word[index]
            if ch == '.':
                for key in node:
                    if key != '#' and dfs(index+1, node[key]):
                        return True
                return False
            if ch in node:
                node = node[ch]
                return dfs(index + 1, node)
            else:
                return False

        node = self.trie
        return dfs(0, node)

