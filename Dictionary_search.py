describe_people2= dict(ligga='L', Hawsha = 'Homeboi', Munees = "Playboi", Manja = 'Manja', Preetam = "Preeti")

def linear_search(dict,value):
    for key in dict:
        if dict[key] == value:
            print(key,':',value)
linear_search(describe_people2,'L')