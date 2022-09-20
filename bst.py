#class called node 
class Node(object): #object is the primitive class, so i inherit
    pass
    
    #left riight and kwy
    def __init__(self, key):
         self.left = None
         self.right = None
         self.key = key #this is a root nodee
         
        


#def insert
    def insert(self, key):
        #we we already have root node\
        if(self.key):
        # then check left and right
            #condition 1: if less then go left
            if(key<self.key):
                #condition1 if left is nill, fill the value
                if(self.left==None):
                    self.left =Node(key)
                #condition 2 if the left is no nill  consider left as the parent
                else:
                    self.left.insert(key)
            #conditon 2: if grater then go right
            elif(key>=self.key):
                if(self.right==None):
                    self.right= Node(key)
                else:
                    self.right.insert(key)
        #if no root node this key is the root node
        else:
            self.key =key
        

#try our class

#def printTree
    def printT(self):
        
        if(self.left):
            self.left.printT()
        print(self.key)
        if(self.right):
            self.right.printT()
#def delete
    def delete(self,key):
        if(self.key==None):
            print("tree is empty")
            return
        if(key < self.key):
            if(self.left):
                self.left=self.left.delete(key)
            else:
                print("The givne node is not present in the tree-LEFT")
        elif(key>=self.key):
            if(self.right):
                self.right=self.right.delete(key)
            else:
                print("The given node is not present in the tree")
        else:
            if (self.left==None):
                temp =self.right
                self =None
                return temp
            if (self.right==None):
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key=node.key
            self.right=self.right.delete(node.key)
        return self
            
            
            
        
root = Node(10)
root.insert(11)
root.insert(5)
root.insert(3)
root.delete(10)
root.printT()


