import iso6346

class ShippingContainer:

    next_serial = 1337

    # this can access other class methods or constructor
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

    # used as factory method
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents = [])

    # used as factory method
    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents = list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code = owner_code,
            serial = ShippingContainer._generate_serial()
        )
        

container = ShippingContainer.create_empty("YML")
print(container.contents)
print(container.bic)

container2 = ShippingContainer.create_with_items("YML", ['tools', 'food', 'cars'])
print(container2.contents)
print(container2.bic)
