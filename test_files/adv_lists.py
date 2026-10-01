passwords = [
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'},
    #{'service': 'michael', 'password': 'password123', 'added_on': '22/03/22'},
    #{'service': 'slop', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

# -----------------------------------------------------------------------------------------
# Version 1

def are_all_passwords_long_enough_1(passwords):
    for password in passwords:
        if len(password['password']) < 8:
            return False
    return True

#print(are_all_passwords_long_enough_1(passwords))

# -----------------------------------------------------------------------------------------
# Version 2

def is_too_short(password):
    return len(password['password']) < 8

def are_all_passwords_long_enough_2(passwords):
    return len(list(filter(is_too_short, passwords))) == 0

#print(are_all_passwords_long_enough_2(passwords))

# -----------------------------------------------------------------------------------------
# Version 2.1

def are_all_passwords_long_enough_2_1(passwords):
    return list(filter(lambda password: len(password['password']) < 8, passwords)) == []

#print(are_all_passwords_long_enough_2_1(passwords))

# -----------------------------------------------------------------------------------------
# Version 3

def are_all_passwords_long_enough_3(passwords):
    return len([password for password in passwords if len(password['password']) < 8]) == 0

#print(are_all_passwords_long_enough_3(passwords))

# -----------------------------------------------------------------------------------------
# My turn :tongue:
# Version 1

def added_on_21_1(passwords):
    for pwd in passwords:
        if pwd['added_on'] == '21/03/22':
            return True
    return False

#print(added_on_21_1(passwords))

def pass_on_22_1(passwords):
    pwds = []
    for pwd in passwords:
        if pwd['added_on'] == '22/03/22':
            pwds.append(pwd['service'])
    return pwds

# print(f"Services added on 22/03/22: {', '.join((pass_on_22_1(passwords)[:-1])).title()}, and {pass_on_22_1(passwords)[-1].title()}")


# -----------------------------------------------------------------------------------------
# Version 2

def is_it_added_on_21(pwd):
    return pwd['added_on'] == '21/03/22'

def added_on_21_2(passwords):
    return len(list(filter(is_it_added_on_21, passwords))) > 0

#print(added_on_21_2(passwords))

def create_pass_list(pwd):
    return pwd['added_on'] == '22/03/22'

def pass_on_22_2(passwords):
    pwds = []
    for pwd in list(filter(create_pass_list, passwords)):
        pwds.append(pwd['service'])
    return pwds

# print(f"Services added on 22/03/22: {', '.join((pass_on_22_2(passwords)[:-1])).title()}, and {pass_on_22_2(passwords)[-1].title()}")

# -----------------------------------------------------------------------------------------
# Version 2.1

def added_on_21_2_1(passwords):
    return len(list(filter(lambda pwd: pwd['added_on'] == '21/03/22', passwords))) > 0

#print(added_on_21_2_1(passwords))

def pass_on_22_2_1(passwords):
    pwds = []
    for pwd in list(filter(lambda pwd: pwd['added_on'] == '22/03/22', passwords)):
        pwds.append(pwd['service'])
    return pwds

# print(f"Services added on 22/03/22: {', '.join((pass_on_22_2_1(passwords)[:-1])).title()}, and {pass_on_22_2_1(passwords)[-1].title()}")

# -----------------------------------------------------------------------------------------
# Version 3

def added_on_21_3(passwords):
    return len([pwd for pwd in passwords if pwd['added_on'] == '21/03/22']) > 0

#print(added_on_21_3(passwords))

def pass_on_22_3(passwords):
    return [pwd['service'] for pwd in passwords if pwd['added_on'] == '22/03/22']
    
#print(f"Services added on 22/03/22: {', '.join((pass_on_22_3(passwords)[:-1])).title()}, and {pass_on_22_3(passwords)[-1].title()}")
