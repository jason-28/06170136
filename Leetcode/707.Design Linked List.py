class node:
        
    def __init__(self,value): 
            self.val=value
            self.next=None
            
class MyLinkedList:

    def __init__(self):
       
        self.head=None
        self.len=0

    def get(self, index: int) -> int:

        if index<0 or index>=self.len: 
            return -1
        else:
            value = self.head
            for _ in range(index):
                value = value.next
            return value.val

    def addAtHead(self, val: int) -> None:
 
        N_head=node(val)
        if self.len==0:
            self.head=N_head
        else:
            N_head.next=self.head
            self.head=N_head
        self.len+=1
      
    def addAtTail(self, val: int) -> None:
     
        N_tail=node(val)
        if self.len==0:
            self.head=N_tail
        else:
            value=self.head
            for i in range(self.len):
                if value.next!=None:
                    value=value.next
                else:
                    break
            value.next=N_tail
        self.len+=1
            
    def addAtIndex(self, index: int, val: int) -> None:
    
        add_node=node(val)
        if index>self.len:
            return -1
        elif index<=0 or self.len==0:
            self.addAtHead(val)
        else:
            value=self.head
            for i in range(self.len):
                if i==(index-1):
                    add_node.next=value.next 
                    value.next=add_node     
                else:
                    value=value.next 
            self.len+=1

    def deleteAtIndex(self, index: int) -> None:
 
        if index>=self.len or self.len==0 or index<0:
            return -1
        
        elif index==0:
            value = self.head
            self.head = value.next
            self.len-=1
        
        elif self.len==1:
            self.head=None
            self.len=0
                
        else:
            value = self.head
            for i in range(index):
                if i==(index-1):
                    del_node=value.next 
                    value.next=del_node.next
                else:
                    value = value.next 
            self.len-=1
