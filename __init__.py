from .base import Bus


def get_bus():

    from .mraa import I2c

    return Bus(I2c)

