class Node:    
    def __init__(self,cargo=None,left=None,right=None):
        self.left= left
        self.right= right        
        self.cargo= cargo


    def __str__(self):
        return str(self.cargo)


import time as t


class Binary_Search_Tree:   
    def __init__(self,root=None):
        self.root= root
    
    
    def inserter(self,value):
        if self.root== None: 
            self.root= Node(value)       
        else:           
            self.inserter_help(self.root,value)
           
           
    def inserter_help(self,current,value):
        if value> current.cargo:
            if current.right!= None:               
                self.inserter_help(current.right,value)
            else:
                current.right= Node(value)        
        elif value< current.cargo:
            if current.left!= None:
                self.inserter_help(current.left,value)
            else:
                current.left = Node(value)

                
    def search(self,value):
        point= self.searcher_help(self.root,value) 
        time_start= t.perf_counter() 
        print(dtype(value))
        time_end= t.perf_counter()
        count= str(time_end-time_start)
        print("time taken:"+ count)
        return point
   
   
    def searcher_help(self,current,value):
        if current.cargo== None:
            return False
        elif value== current.cargo:            
            return True
        if value> current.cargo:
            self.searcher_help(current.right,value)        
        if value< current.cargo:
            self.searcher_help(current.left,value)


def constructBST(fileName):
    file= open(fileName,"r")       
    line= file.readlines()
    search= Binary_Search_Tree()
    for i in range(len(line)):
        search.inserter(line[i])
        file.close()
    return search


if __name__ == "__main__":
    fname= "websites.txt"
    search= constructBST(fname)
   
