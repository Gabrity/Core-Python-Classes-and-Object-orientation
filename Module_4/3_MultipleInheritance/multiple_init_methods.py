class Base1:
    def __init__(self):
        print('base1.__init__')
              
class Base2:    
    def __init__(self):
        print('base2.__init__')

class Child(Base1, Base2):
    pass
    

s = Child() # only base1 initializer is called if it is not specified
#result:
#base1.__init__
