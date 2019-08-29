# Finding Length of the tree

def length(self):
        if self.value == None:
            return(0)
        elif self.next == None:
            return(1)
        else:
            return(1+self.next.length())
a=[13,12,11,23,45,54,65,34,54]

