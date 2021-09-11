simbolos = 'ΕεΘΠξτΙΠΡΥἁᾰΆ'


code = []

for simbolo in simbolos:
    code.append(ord(simbolo))

print(code)

# usando list compreension

codigo = []

codigo = [ord(simbolu) for simbolu in simbolos]

print(codigo)
