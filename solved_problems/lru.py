# https://leetcode.com/problems/lru-cache/
class link:
    def __init__(self,key,val):
        self.l = None
        self.r = None
        self.val = val
        self.key = key
        

class LRUCache:

    def __init__(self, capacity):
        self.c = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.dic:
            temp = self.dic[key]
            if self.head.key != temp.key:
                if self.tail.key == temp.key:
                    self.tail = temp.l
                temp.l.r = temp.r
                if temp.r:
                    temp.r.l = temp.l
                temp.l = None
                temp.r = self.head
                self.head = temp
                temp.r.l = temp
            return temp.val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.dic:
            self.dic[key].val = value
            t = self.get(key)
        else:
            temp = link(key,value)
            temp.r = self.head
            self.head = temp
            self.dic[key] = temp
            if len(self.dic) == 1:
                self.tail = temp
            else:
                temp.r.l = temp
            if len(self.dic) > self.c:
                key = self.tail.key
                prev = self.tail.l
                prev.r = None
                self.tail = prev
                del self.dic[key]
                