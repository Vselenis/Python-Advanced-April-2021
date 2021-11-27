import re

letter_path = r"[a-z]"
punctuation_path = r"[',\.\!\?-]"

def get_n(line, path):
    return len(re.findall(path, line, re.IGNORECASE))


with open("text.txt", "r") as file:
    lines = file.readlines()
    for line in range(len(lines)):
        n_letters = get_n(lines[line], letter_path)
        n_punctuation = get_n(lines[line], punctuation_path)
        print(f"Line {line+1}: {lines[line]} ({n_letters})({n_punctuation})")