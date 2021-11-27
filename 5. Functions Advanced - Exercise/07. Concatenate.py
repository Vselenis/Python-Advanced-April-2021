def concatenate(*args):
    split_words = ''
    for word in args:
        split_words += word
    return split_words


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
