class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:
    def __init__(self,capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right = Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self, node):
        prev,next = node.prev, node.next
        prev.next=next
        next.prev=prev

    
    def insert(self, node):
        prev= self.right.prev
        next=self.right
        prev.next = next.prev = node
        node.next, node.prev=next,prev 
        


    def get(self,key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1


    def put(self,key:int, value:int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cahce[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

