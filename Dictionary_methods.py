mydict= dict(name='Sashreek',Age='17',Sex='Male')
nodict= dict(pp='Yes')
new_dict= mydict.copy()
print(mydict)
print(new_dict)
another= mydict.fromkeys(['name','age','Kit'],2)
print(another)
di=mydict.get('name',2)
print(di)
it=mydict.items()
print(it)
print(mydict.keys())
print(mydict.setdefault('Uni','Alberta'))
print(mydict)
mydict.update(nodict)
print(mydict)