lax_coordinates = (22.9425, -118.408056)

city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)

traveler_ids = [("USA", '32323242'), ("BRA", "804890234"), ("ESP", 'XEDA3934')]

for passaport in sorted(traveler_ids):
    print('%s %s' % passaport)

for country, _ in traveler_ids:  # como a tupla tem dois valores mas o iteresse so se da em um usamo o _ para comunicar isso para o python
    print(country)
