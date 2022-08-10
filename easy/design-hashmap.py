# Design a hash map without dictionary and hash libraries

class Bucket:
    def __init__(self):
        self._keys = []
        self._values = []
        
    def put(self, key, value):
        for i in range(len(self._keys)):
            if self._keys[i] == key:
                self._values[i] = value
                return None
        
        self._keys.append(key)
        self._values.append(value)
                
    def get(self, key):
        for i in range(len(self._keys)):
            if self._keys[i] == key:
                return self._values[i]
        return -1
    
    def remove(self, key):
        for i in range(len(self._keys)):
            if self._keys[i] == key:
                del self._keys[i]
                del self._values[i]
                break

class HashMap:
    def __init__(self, size = 2560):
        self.size = size
        self._map = [Bucket() for i in range(size)]

    def __hash(self, key):
        return key % self.size
        
    def put(self, key, value):
        k = self.__hash(key)
        return self._map[k].put(key, value)
        
    def get(self, key):
        k = self.__hash(key)
        return self._map[k].get(key)
        
    def remove(self, key):
        k = self.__hash(key)
        return self._map[k].remove(key)
        
hmap = HashMap()
hmap.put(1, 'hello')
hmap.put(2, 'buy')
hmap.put(12, 'hi again')
print(hmap.get(3) == -1)
print(hmap.get(1) == 'hello')
hmap.remove(1)
print(hmap.get(1) == -1)