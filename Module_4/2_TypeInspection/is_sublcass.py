from simple_list import *

print(issubclass(IntList, SimpleList))
print(issubclass(SimpleList, IntList))

class MyInt(int): pass
class MySpecialInt(MyInt) : pass
print(issubclass(MySpecialInt, int))
