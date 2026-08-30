class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap to store {key : pointer to node}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update LRU: remove from list and add to the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # insert, then check capacity to remove from the left
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
'''
key-value : hashmap
doubly linked list: insertion and deletion will only be updating pointers, requires 2ptrs to track LRU and most recent
any call on the key makes it most recent -> need to move the node to the most recent side (right side)
left -> nodes -> right
hashmap key : pointer to the node
node: key, value, prev, next
'''