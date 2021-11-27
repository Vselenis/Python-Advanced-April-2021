result = [el for data in input().split("|")[::-1] for el in data.split(" ")if el != ""]
print(' '.join(result))