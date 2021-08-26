class node:
    def __init__(self,name):
        self.name=name
        self.children=[]
        self.parent=None
    
    def addchild(self,child):
        child.parent=self
        self.children.append(child)
    
    def level(self):
        level=0
        i=self.parent
        while i:
            level+=1
            i=i.parent
        return level

    def print_tree(self,l):
        if self.level()<=l:
            spaces='   '*self.level()
            prefix=spaces+'|---'
            print(self.name,f'({l})') if self.level()==0 else print(prefix,self.name,sep='')

        for i in self.children:
            i.print_tree(l)

def build_location_tree():
    root=node('Global')
    l1=node('India')
    a=node('Gujrat')
    a.addchild(node('Ahmedabad'))
    a.addchild(node('Baroda'))
    b=node('Karnataka')
    b.addchild(node('Bangluru'))
    b.addchild(node('Mysore'))
    l1.addchild(a)
    l1.addchild(b)
    root.addchild(l1)

    l1=node('USA')
    a=node('New Jersey')
    a.addchild(node('Princeton'))
    a.addchild(node('Trenton'))
    b=node('California')
    b.addchild(node('San Francisco'))
    b.addchild(node('Mountain View'))
    b.addchild(node('Palo Alto'))
    l1.addchild(a)
    l1.addchild(b)
    root.addchild(l1)
    return root

if __name__=='__main__':
    root=build_location_tree()
    print()
    root.print_tree(0)
    print()
    root.print_tree(1)
    print()  
    root.print_tree(2)
    print()  
    root.print_tree(3)
    