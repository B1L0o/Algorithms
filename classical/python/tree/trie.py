# Also known as PrefixTree
class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_ending = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def add_word(self,word):
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if current.children[index] == None:
                current.children[index] = TrieNode()
            current=current.children[index]
        current.is_ending = True
    

    def is_present(self,word):
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if current.children[index] == None:
                return False
            current=current.children[index]
        return current.is_ending
    

    def is_prefix(self,word):
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if current.children[index] == None:
                return False
            current=current.children[index]
        return True


if __name__ == "__main__":
    prefixTree = Trie() 
    prefixTree.add_word("banana")
    print(prefixTree.is_present("banana"))
    print(prefixTree.is_prefix("bana"))
    print(prefixTree.is_prefix("banab"))