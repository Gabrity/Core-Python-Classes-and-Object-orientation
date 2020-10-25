import iso6346

class ShippingContainer:

    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    FRIDGE_VOLUME_FT3 = 100

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents = [], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents = list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code = owner_code,
            serial = ShippingContainer._generate_serial()
        )

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
        
class RefigiratedShippingContainer(ShippingContainer):
    
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 +32
        
    @staticmethod
    def _f_to_c(farenheit):
        return farenheit - 32 *5/9

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value > RefigiratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Too hot!')
        self._celsius = value

    @property
    def farenheit(self):
        return RefigiratedShippingContainer._c_to_f(self.celsius)
    
    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefigiratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return (super().volume_ft3 - RefigiratedShippingContainer.FRIDGE_VOLUME_FT3)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category='R'
        )
        

class HeatedRefigiratedShippingContainer(RefigiratedShippingContainer):
    
    MIN_CELSIUS = -20

    @RefigiratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefigiratedShippingContainer.MIN_CELSIUS:
            raise ValueError('Too cold!')
        RefigiratedShippingContainer.celsius.fset(self, value)


container = ShippingContainer.create_empty("YML", 20)
print(container.volume_ft3)

container = RefigiratedShippingContainer.create_empty("YML", 20, celsius = -10)
print(container.volume_ft3)

container = HeatedRefigiratedShippingContainer.create_empty("YML", 20, celsius = -20)
print(container.volume_ft3)

