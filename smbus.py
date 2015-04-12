import smbus

class I2c(smbus):
    """ The smbus module is more flexible, but we want to pin it down to a specific bus
    """

    id = None
    address = None

    def read(self):
        self.
