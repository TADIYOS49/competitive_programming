class MyLinkedList:

    def __init__(self):
        # print("----------------------")
        new = ListNode()
        self.x = new.next
         

    def get(self, index: int) -> int:
        count = 0
        temp = self.x
        while temp:
            if index == count:
                return temp.val
            count +=1
            temp = temp.next
        return -1
        
    def addAtHead(self, val: int) -> None:
        add = ListNode(val,self.x)
        self.x = add
        
        

    def addAtTail(self, val: int) -> None:
        temp = self.x
        if temp == None:
            add = ListNode(val,self.x)
            self.x = add
        else:
            while temp and temp.next:
                temp = temp.next
            add = ListNode(val)
            temp.next = add
       

    def addAtIndex(self, index: int, val: int) -> None:
        
        temp = self.x
        if index == 0:
            self.addAtHead(val)
        else:
            while temp and index != 1:
                temp = temp.next
                index -= 1
            add = ListNode(val)
            if temp :
                add.next = temp.next
                temp.next = add
            else:
                temp = add
            
        

    def deleteAtIndex(self, index: int) -> None:
        temp = self.x
        
        if index == 0:
            self.x= self.x.next
        else:
            while temp and index != 1:
                temp = temp.next
                index -=1
            if temp and temp.next:
                temp.next = temp.next.next
            else:
                temp = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)