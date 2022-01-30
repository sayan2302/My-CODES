class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linked_list:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.insert_at_beginning(data)
            return
        i=self.head
        while i.next:
            i=i.next
        i.next=new_node
    def print(self):
        if self.head==None:
            print("Empty LL")
            return
        i=self.head
        string=''
        while i:
            string+=str(i.data)+'-->'
            i=i.next
        print(string[:-3])
    def clear(self):
        self.head=None
    def insert_values(self,*l):
        for i in l:
            self.insert_at_end(i)
    def length(self):
        c=0
        i=self.head
        while i:
            c+=1
            i=i.next
        return(c)
    def insert_at_index(self,data,pos):
        if pos<0 or pos>self.length():
            raise Exception('Wrong Index')
        c=0
        i=self.head
        if pos==0 or i==None:
            self.insert_at_beginning(data)
            return
        while i:
            if c==pos-1:
                next_element=i.next
                i.next=Node(data,next_element)
                return
            i=i.next
            c+=1
    def replace_at_index(self,data,pos):
        if self.head==None:
            raise Exception('Empty LL')
        if pos<0 or pos>self.length()-1 :
            raise Exception('Wrong Index')
        c=0
        i=self.head
        if pos==0:
            i.data=data
            return
        for _ in range(pos):
            i=i.next
        i.data=data
    def remove_at_index(self,pos):
        if self.head==None:
            raise Exception('Empty LL')
        if pos<0 or pos>self.length()-1:
            raise Exception('Wrong Index')
        i=self.head
        if pos==0:
            i=i.next
        for _ in range(pos-1):
            i=i.next
        i.next=i.next.next
        
if __name__ == '__main__':
    ll=linked_list()
    ll.insert_at_beginning(23)
    ll.insert_at_beginning(2)
    ll.insert_at_end(45)
    # print(ll.length()) 
    ll.insert_values(0,1,2,18)
    ll.clear()
    ll.insert_values(7,5,3,6)
    ll.print()
    ll.remove_at_index(2)
    ll.print()
