# Rationale

Looks to me like i2c with Python is a mess. You use a different module depending on what platform you're on, and their interfaces are all their own.

This repository ties them together and provides a uniform interface with which to access them.

# The Goods

Here's what you get;

A class that represents a single bus.

    from Pi2c import I2c
    
    I2c(bus_number)

With this class, you can access slaves.

    I2c.read(address, sub_address)
    
    I2c.write(address, sub_address, data)
