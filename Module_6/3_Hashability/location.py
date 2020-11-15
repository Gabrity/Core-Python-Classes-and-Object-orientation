from dataclasses import dataclass
#from position import Position, EarthPosition

# it is hard to create hasable types, while dictionary and set requires them to be hashable
# dataclasses are best used as immutable, so:
# 1. dataclasses should also only contain immuatble attributes
# 2. it should be declared as frozen (immutable) 


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class Location:
    name: str
    position: int

hong_kong = Location("Hong Kong",114.16)
stockholm = Location("Stockholm",54.9)

# does not work if forzen = False
my_set = {hong_kong, stockholm}