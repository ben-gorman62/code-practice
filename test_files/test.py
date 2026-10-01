class Person():
    def __init__(self, name, birthday, favourite_language):
        self.name = name
        self.birthday = birthday
        self.favourite_language = favourite_language

person1 = Person("Alan Turing", "June 23", "Standard Description")
person2 = Person("Ada Lovelace", "December 10", "n/a")
person3 = Person("Grace Hopper", "December 9", "COBOL")
person4 = Person("John von Neumann", "December 28", "C")
person5 = Person("Claude Shannon", "April 30", "C")

print(person2.birthday)

s = [None, None, None, None, None]

def remove_nones_from_list(list):
    for x in list[::-1]: 
        if x == None:
            list.remove(x)
    return list

remove_nones_from_list(s)


def add(l, i):
    l.append(i)
    print(l)
add(['a', 'b', 'c'], 'd')


#def new_band_member(member):
#    band = {"vocalist": "miss piggy", "lead_guitar": "scooter"}
#    return band + member
#new_band_member({"bass": "John"})


def remove_nones_from_dictionary(dict):
    for entry in dict.items():
        if None in entry:
            print(entry)
            
    return dict

remove_nones_from_dictionary({'one': None, 'three': 3, 'two': 2})


prices = [1.13, 1.13, 1.13, 4.27, 8.88]
#print(sum(round(p * 1.20, 2) for p in prices))
#print(0.1+0.2)

import decimal

def total_with_vat(prices):
    print(prices)
    for p in prices:
        p * 100
    print(round(sum(prices) * 1.20, 2))

total_with_vat(prices)

