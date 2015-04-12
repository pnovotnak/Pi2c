from i2c.backends.base import Bus


class I2c(mraa.I2c, Bus):
    """ Binds to an mraa object and provides an interface to interact with the bus.

    Since mraa is well written, we basically just provide the class verbatim
    """

    def read(self, address, sub_address):
        self.address(address)
        return super(I2c, self, sub_address)

    def write(self, address, sub_address, data):
        self.address(address)
        return super(I2c, self).write(sub_address, data)
