class Position:

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

    @property
    def latitude_hemisphere(self):
        return 'N' if self.latitude >= 0 else 'S'

    @property
    def longitude_hemisphere(self):
        return 'E' if self.longitude >= 0 else 'W'

    # str is the string constructor, it takes any object
    # it should be user readable and aesthetic for external representation
    def __str__(self):
        return (
            f"{abs(self.latitude)} {self.latitude_hemisphere}, "
            f"{abs(self.longitude)} {self.longitude_hemisphere}"
            )

def typename(obj):
    return type(obj).__name__

class MarsPosition(Position):
    pass

class EarthPosition(Position):
    pass


oslo_position = Position(-45, 179)
print(str(oslo_position))

