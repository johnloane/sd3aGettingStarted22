words = set()


def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True


def size():
    return len(words)


load("wordlist.10000.txt")
if check("Python"):
    print("Dictionary contains Python")
else:
    print("Dictionary does not contain python")

print(f"The dictionary has {size()}")


