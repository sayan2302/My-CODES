class Node:
    def _init_(self,data=None,next=None):
        self.data=data
        self.next=next

class llist:
    def _init_(self,head=None):
        self.head=head   
    def print(self):
        if self.head==None:
            print("empty linked list")
            return
        i=self.head
        x='['
        while i:
            x+=str(i.data)+','
            i=i.next
        print(x[:-1]+']')
    def insert_begin(self,data):
        node=Node(data,self.head)
        self.head=node
        return       
    def insert_last(self,data):
        node=Node(data,None)
        if self.head==None:
            self.head=node
            return
        i=self.head
        while i.next:
            i=i.next
        i.next=node
    def insert_values(self,list):
        #self.head=None   #to clear the LL before entering the data list
        for i in list:
            self.insert_last(i)    
    def length(self):
        c=0
        i=self.head
        while i:
            c+=1
            i=i.next
        return c
    def remove_element_at(self,pos):
        i=self.head
        x=0
        if pos<0 or pos>self.length()-1:
            raise Exception('wrong Index')
        while i:
            if x==pos-1:
                i.next=i.next.next
                break
            x+=1
            i=i.next  
    def clear_all(self):
        self.head=None
        return
    def insert_element_at(self,data,pos):
        if pos<0 or pos>self.length()-1:
            raise Exception('Wrong Index')
        x=0
        while self.head:
            if pos==0:
                self.insert_begin(data)
                return
            if x==pos-1:
                self.head.next=Node(data,self.head.next)
                return
            x+=1
            self.head=self.head.next
    def replace_element_at(self,data,pos):
        if pos<0 or pos>self.length()-1:
            raise Exception('Wrong Index')
        x=0
        while self.head:
            if pos==0:
                self.head.data=data
                return
            if x==pos-1 or pos==0 :
                self.head.next=Node(data,self.head.next.next)
                break
            x+=1
            self.head=self.head.next

ll=llist()
ll.insert_last(78)
ll.insert_begin(54)
ll.insert_last(23)
ll.clear_all()
ll.insert_values([2,3,4,5,6,7,8,9])
print(ll.length())
ll.remove_element_at(2)
ll.insert_element_at('sayan',0)
ll.replace_element_at('aman',0)
ll.print()
