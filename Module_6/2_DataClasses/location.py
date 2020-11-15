from dataclasses import dataclass
#needs equality defined on Position:
#from position import Position, EarthPosition


# dataclass decorator is used to generate properties for classes automatically 

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Location:
    name: str
    position: int

hong_kong = Location("Hong Kong",114.16)
print(hong_kong)
some_city = Location("Hong Kong", 114.16)
print(hong_kong == some_city)