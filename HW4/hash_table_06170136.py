from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
      
    
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
     
    def hexdigest(self,str): 
        h=MD5.new() 
        h.update(str.encode("utf-8")) 
        num=int(h.hexdigest(),16) 
        return num 
    
    def add(self, key):
        num=self.hexdigest(key)
        i=num%self.capacity
        cur=self.data[i]
        self.data[i]=ListNode(num)
        if cur!=None:
            if cur.val==num:
                pass
            
    def remove(self, key):
        num=self.hexdigest(key)
        i=num%self.capacity
        cur=self.data[i]
        
        while cur!=None:
            if cur.val==num:
                self.data[i]=cur.next
                return
            else:
                cur=cur.next
            return
        
    def contains(self, key):
        num=self.hexdigest(key)
        i=num%self.capacity
        cur=self.data[i]
        while cur!=None:
            if cur.val==num:
                return True
            cur=cur.next
        return False
