'''''Define a function to count the frequency of words in a given list of words.

'''''

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

''''Output:

 {'apple': 3, 'orange': 2, 'banana': 1} '''''

def frequency_count(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)

frequency_count(words)


'''''Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
'''''
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value
    return dict1
print(merge_dicts(dict1,dict2))


'''''Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.'''''
my_dict = {'a': 5, 'b': 9, 'c': 2}
def max_value(dict):
    for value in dict.values():
        if value == max(dict.values()):
            return value
print(max_value(my_dict))

'''''
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.'''''

def reverse_dict(dict):
    new_dict= {}
    for key, value in dict.items():
        new_dict[value]= key
    return new_dict
print(reverse_dict(my_dict))

'''''Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
'''''

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 



