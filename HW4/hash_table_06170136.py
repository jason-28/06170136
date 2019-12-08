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
        if self.contains(key) is False:
            num=self.hexdigest(key)
            i=num%self.capacity
            cur=self.data[i]
            if cur==None:
                self.data[i]=ListNode(num)
            else:
                while cur!=None:
                    if cur.next==None:
                        cur.next=ListNode(num)
                    else:
                        cur=cur.next
                        return
        else:
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
