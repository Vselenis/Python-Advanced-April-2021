n, m = map(int, input().split())
elements_n = set()
elements_m = set()

for _ in range(n):
    set_n = input()
    elements_n.add(set_n)

for _ in range(m):
    set_m = input()
    elements_m.add(set_m)

for x in elements_n:
    if x in elements_m:
        print(x)
