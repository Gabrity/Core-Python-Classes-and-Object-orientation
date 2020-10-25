import iso6346

class ShippingContainer:

    next_serial = 1337

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
    def create_empty(cls, owner_code):
        return cls(owner_code, contents = [])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents = list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # this would not work in a polyophic way, but the base method would be called
        # self.bic = ShippingContainer._make_bic_code(
        self.bic = self._make_bic_code(
            owner_code = owner_code,
            serial = ShippingContainer._generate_serial()
        )
        
class RefigiratedShippingContainer(ShippingContainer):
    
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category='R'
        )

c = ShippingContainer.create_with_items("YML", ['fish'])
print(c._make_bic_code("YML", 1234))

r = RefigiratedShippingContainer.create_with_items("YML", ['fish'])
print(r._make_bic_code("YML", 1234))

container = RefigiratedShippingContainer.create_with_items("YML", ['fish'])
print(container.bic)


