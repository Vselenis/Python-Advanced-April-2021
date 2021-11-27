vowels = {'a', 'o', 'u', 'e', 'i'}
[vowels.add(x.upper()) for x in list(vowels)]

elements = [ch for ch in input() if ch not in vowels]

print("".join(elements))