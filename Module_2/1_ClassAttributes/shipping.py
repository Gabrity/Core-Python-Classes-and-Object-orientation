class ShippingContainer:

    next_serial = 1337 # this is a class attribute

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code # this is an instance attribute 
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        # this would create a new instance attribute which hides the class attribute
        # self.next_serial += 1 
        

container = ShippingContainer('MAE', ['tools'])
container2 = ShippingContainer('MAE', ['cars'])

print(container2.serial)