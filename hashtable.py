class HashTable:
    """
    Hash table class.

    :param size: Size of the hash table.
    """
    GA_RATIO = (5 ** 0.5 - 1) / 2

    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]

    def addKey(self, key: str):
        index = self.calcKey(key)
        self.table[index].append(key)

    def calcKey(self, key: str) -> int:
        hash_value = sum(ord(char) * (self.GA_RATIO ** i) for i, char in enumerate(key, 1))
        return int(self.size * (hash_value % 1))

    def delKey(self, key: str):
        index = self.calcKey(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def getHashTable(self) -> list:
        return self.table

    def getKey(self, key: str) -> int:
        index = self.calcKey(key)
        if key in self.table[index]:
            return index
        else:
            return None
        
    def searchKey(self, key: str) -> bool:
        index = self.calcKey(key)
        if key in self.table[index]:
            return True
        else:
            return False
        
    
if __name__ == "__main__":
    hashTable = HashTable(10)
    hashTable.addKey("AJKDSJFPDAS")
    hashTable.addKey("B")
    hashTable.addKey("C")

    key_index_a = hashTable.getKey("AJKDSJFPDAS")
    key_index_b = hashTable.getKey("B")
    key_index_c = hashTable.getKey("C")

    print(f"Index: {key_index_a}, Value: {hashTable.table[key_index_a]}")   
    print(f"Index: {key_index_b}, Value: {hashTable.table[key_index_b]}")
    print(f"Index: {key_index_c}, Value: {hashTable.table[key_index_c]}")
