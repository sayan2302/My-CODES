class node:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    
    def addchild(self,childnode):
        childnode.parent=self
        self.children.append(childnode)

    def level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self,param):
        prefix='   '*self.level() + '|---'
        if param.casefold()=='name':
            print(prefix,self.name)if self.level()!=0 else print(self.name)
        elif param.casefold()=='designation':
            print(prefix,self.designation)if self.level()!=0 else print(self.designation)
        elif param.casefold()=='both':
            print(prefix,self.name,f'({self.designation})')if self.level()!=0 else print(self.name,f'({self.designation})')
        for i in self.children:
            i.print_tree(param)
def build_management_tree():
    root_node=node('nilupul','CEO')
    a=node('Chinmay','CTO')
    b=node('Vishwa','Infrastructure Head')
    b.addchild(node('Dhaval','Cloud Manager'))
    b.addchild(node('Abhijit','App Manager'))
    c=node('Aamir','Application Head')
    a.addchild(b)
    a.addchild(c)
    root_node.addchild(a)
    a=node('Gels','HR Head')
    a.addchild(node('Peter','Recruitment Manager'))
    a.addchild(node('Waqas','Policy Manager'))
    root_node.addchild(a)
    return root_node

if __name__=='__main__':
    root_node=build_management_tree()
    root_node.print_tree("name")
    print()
    root_node.print_tree("designation")
    print()
    root_node.print_tree("both")