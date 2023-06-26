class MapSum(object):

    def __init__(self):
        self.dict = {}


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.dict[key] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        s = 0
        for key, val in self.dict.items():
            if key.startswith(prefix):
                s += val
        return s



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
