n = int(input())
chemical_compounds = set()
for _ in range(n):
    compounds = input().split()
    for x in compounds:
        chemical_compounds.add(x)

[print(el) for el in chemical_compounds]
