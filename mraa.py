import mraa

from .base import Bus


class I2c(mraa.I2c, Bus):
    """ Binds to an mraa object and provides an interface to interact with the bus.

    Since mraa is well written, we basically just provide the class verbatim
    """

    pass
