# expressoes geradoras

cores = ["preto", "branco"]

tamanhos = ["S", "M", "L"]

for camisa in ("%s %s" % (c, t) for c in cores for t in tamanhos):
    print(camisa)
