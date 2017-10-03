def func(r,b):

    alphabet = range(r)
    base = b
    return dict((x*base**2+y*base+z,(x,y,z)) for x in alphabet
    for y in alphabet
    for z in alphabet )

func(1000, 10)