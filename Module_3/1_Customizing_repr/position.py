addeclass Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    # this is used to display data in the repl
    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

def typename(obj):
    return type(obj).__name__

class MarsPosition(Position):
    pass

class EarthPosition(Position):
    pass


# these two produce the same
oslo_position = Position(-45, 179)
print(repr(oslo_position))
print(oslo_position)

# eval produces not the same type
p = eval(repr(oslo_position))
print(p.latitude)

# as general rules, in repr try to:
# include all important state
# format as if it was a constructor parameter list => eval can be executed as python source code

manua_kea = EarthPosition(19.82, -155.47)
print(repr(manua_kea))

olympus_mons = MarsPosition(18.65, -133.8)
print(repr(olympus_mons))
