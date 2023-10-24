
class Node():
    def __init__(self,value) -> None:
        '''
        root : str
        '''
        self.Value=value
        self.Right=None
        self.Left=None
        
    def add(self,node):
        if self.Left == None:
            self.Left=node
        elif  self.Right == None : 
            self.Right=node

    # def show(self,):
    #     for i in self:
    #         if i.r
            
    #     pass
class BinarySearchTree(object):
    
    def insert(self, root, node):

        if root is None:
            return node
        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
                root.l_child = self.insert(root.l_child, node)
                return root
    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print (root.val)
            self.in_order_place(root.r_child)
    def pre_order_place(self, root):
        if not root:
                return None
        else:
            print (root.val)
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)
    def post_order_place(self, root):
        if not root:
                return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print( root.val)
 
def in_order_print(root):
        if not root:
            return None
        in_order_print(root.Left)
        print(root.Value)
        in_order_print(root.Right)

            
if __name__=='__main__':
    
    
    # s='1+2-5'
    # r=Node('')
    # for i in s:
    #     if i in '+-*/':
            
        
            
    n=Node("miro")
    n.add(Node("serag"))
    n.add(Node('saad'))
    in_order_print(n)
    
    
    


        





