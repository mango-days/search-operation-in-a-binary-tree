# STACK
class Stack :
    def __init__ ( self ): self.array = []
    def push ( self, element ) : self.array.insert( 0 , element )
    def top ( self ) : print ( self.array[0] )
    def empty ( self ) : self.array = []
    def getMin ( self ) : print ( min ( self.array ) )
    def pop ( self ) : 
        print ( self.array[0] )
        self.array.pop ( 0 )
    def printStack ( self ) : print ( self.array )

a = Stack()
for values in range ( 0 , 5 ): a.push(values)
a.printStack()
a.pop()
a.pop()
a.getMin()
a.top()