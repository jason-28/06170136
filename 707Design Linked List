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
 
        Nhead=node(val)
        if self.len==0:
            self.head=Nhead
        else:
            Nhead.next=self.head
            self.head=Nhead
        self.len+=1
      
    def addAtTail(self, val: int) -> None:
     
        Ntail=node(val)
        if self.len==0:
            self.head=Ntail
        else:
            value=self.head
            for i in range(self.len):
                if value.next!=None:
                    value=value.next
                else:
                    break
            value.next=Ntail
        self.len+=1
            
    def addAtIndex(self, index: int, val: int) -> None:
    
        add_item=node(val)
        if index>self.len:
            return -1
        elif index<=0 or self.len==0:
            self.addAtHead(val)
        else:
            value=self.head
            for i in range(self.len):
                if i==(index-1):
                    add_item.next=value.next 
                    value.next=add_item     
                else:
                    value=value.next 
            self.len+=1

    def deleteAtIndex(self, index: int) -> None:
 
        if index>=self.len or self.len==0 or index<0:
            return -1
        elif self.len==1:
            self.head=None
            self.len=0
        elif index==0:
            value = self.head
            self.head = value.next
            self.len-=1
        else:
            value = self.head
            for i in range(index):
                if i==(index-1):
                    del_item=value.next 
                    value.next=del_item.next
                else:
                    value = value.next 
            self.len-=1
