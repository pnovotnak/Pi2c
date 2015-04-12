
try:
    from .backends.mraa import I2c
except ImportError:
    raise ImportError('No compatible I2C backends found.')
