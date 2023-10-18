class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:
    def __init__(self):
        self.dict1 = TrieNode()
        self.dict2 = defaultdict(int)
        
    def insert(self, key, val):
        delta = val - self.dict2[key]
        self.dict2[key] = val
        dict3 = self.dict1

        for i in key:
            if i not in dict3.children:
                dict3.children[i] = TrieNode()

            dict3 = dict3.children[i]
            dict3.score += delta
        
    def sum(self, prefix):
        dict3 = self.dict1

        for i in prefix:
            if i not in dict3.children:
                return 0

            dict3 = dict3.children[i]

        return dict3.score