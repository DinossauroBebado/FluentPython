from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City("Tokyo", 'JP', 36.993, (35.689772, 139.691667))

print(tokyo)

print(tokyo.population)

print(tokyo[1])

print(City._fields)

LatLong = namedtuple("LatLong", "lat long")

delhi_data = ('Delthi NCR', 'IN', 21.935, LatLong(28.613, 77.208))

delhi = City._make(delhi_data)

print(delhi._asdict())
