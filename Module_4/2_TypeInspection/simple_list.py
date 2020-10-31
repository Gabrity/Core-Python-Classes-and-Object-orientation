class SimpleList:

    def __init__(self, items):
        self._items = list(items)
    
    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()
        
    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'    

        
class IntList(SimpleList):
    
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)
    
    def add(self, item):
        self._validate(item)
        super().add(item)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError(f'{x} is not of type int.')


intlist = IntList([3,45,6])
intlist.add(8)
print(intlist)
#intlist.add('4') error
