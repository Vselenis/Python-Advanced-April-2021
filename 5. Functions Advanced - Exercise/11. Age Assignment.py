def age_assignment(*names, **kwargs):
    assigment = {}
    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                assigment[name] = age
    return assigment


print(age_assignment('Amy', 'Bill', 'Willy', W=36, A=22, B=61))
