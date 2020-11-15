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

    def __format__(self, format_spec):
        latitude = format(abs(self.latitude), '.2f')
        longitude = format(abs(self.longitude), '.2f')
        return (
            f"{latitude} {self.latitude_hemisphere}, "
            f"{longitude} {self.longitude_hemisphere}"
            )

def typename(obj):
    return type(obj).__name__

class MarsPosition(Position):
    pass

class EarthPosition(Position):
    pass