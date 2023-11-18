class MapSum:

    def __init__(self):
        self.hash = {}
        self.prefix = {}
        
    def insert(self, key: str, val: int) -> None:
        update=val
        if key in self.hash:
            diff = val - self.hash[key]
            update = diff 
        curPrefix = ""
        for c in key:
            curPrefix += c 
            if curPrefix not in self.prefix:
                self.prefix[curPrefix] = update 
            else:
                self.prefix[curPrefix] += update
        self.hash[key] = val 
        print("self.prefix: ", self.prefix)
    def sum(self, prefix: str) -> int:
        if prefix not in self.prefix:
            return 0 
        return self.prefix[prefix]

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)