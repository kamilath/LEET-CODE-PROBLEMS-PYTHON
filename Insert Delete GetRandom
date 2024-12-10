class RandomizedSet(object):
    def __init__(self):
        self.list=[]
    def insert(self, val):
        if val not in self.list:
            self.list.append(val)
            return True
        return False    
    def remove(self, val):
        if val in self.list:
            self.list.remove(val)
            return True
        return False    
    def getRandom(self):
        return random.choice(self.list)
