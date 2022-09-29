def dec2bin(value):
    ''' Return a list of size 8 containing binary representation of passed integer.'''
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
