#returns highest scoring word when a = 1, b = 2, etc.

def high(x):
    x = x.split(" ")
    best = 0
    for words in x:
        test = 0
        for num in words:
            words = words.lower()
            test += ord(num) - 96
        if test > best:
            best = test
            actual = words
    return actual