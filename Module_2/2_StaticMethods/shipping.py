class ShippingContainer:

    next_serial = 1337 

    # internal implementatio detail of the class, usually not part of the class interface
    # it could be moved to a global a scope
    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        

container = ShippingContainer('MAE', ['tools'])
container2 = ShippingContainer('MAE', ['cars'])

print(container2.serial)