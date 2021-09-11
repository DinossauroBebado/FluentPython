
# genexp

import array
simbolos = 'ΕεΘΠξτΙΠΡΥἁᾰΆ'

print(tuple(ord(simbolo) for simbolo in simbolos))


print(array.array("I", (ord(simbolo)for simbolo in simbolos)))
