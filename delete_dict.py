describe_people2= dict(ligga='L', Hawsha = 'Homeboi', Munees = "Playboi", Manja = 'Manja', Preetam = "Preeti")

del describe_people2['Munees']
print(describe_people2)

remove_element= describe_people2.pop('Hawsha')
print(remove_element)

popitem_ = describe_people2.popitem()
print(popitem_)
print(describe_people2)

describe_people2.clear()
print(describe_people2)