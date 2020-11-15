from dataclasses import dataclass
#from position import Position, EarthPosition

# data classes have a special method that is used for validation of data after the creation of the class
# it runs after init 

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class Location:
    name: str
    position: int

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Name cannot be empty")

null_island = Location("", 0)
