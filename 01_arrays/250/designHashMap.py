class MyHashMap:
    def __init__(self):
        self.store = []

    def put(self, key: int, value: int) -> None:
        replaced = False
        for store in self.store:
            if store[0] == key:
                store[1] = value
                replaced = True
                break
        if not replaced:
            self.store.append([key, value])

    def get(self, key: int) -> int:
        for store in self.store:
            if store[0] == key:
                return store[1]
        
        return -1

    def remove(self, key: int) -> None:
        for store in self.store:
            if store[0] == key:
                self.store.remove(store)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
