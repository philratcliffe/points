from sys import argv
import time

scores = \
    {
        "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10
    }


def findwords():
    letters = argv[1]
    if len(letters) > 7:
        print "Only 7 letters"
        return

    results = {}

    for word in get_next_word():
        if is_winner(word, letters):
            get_score(word)
            results[word] = get_score(word)

    for key in sorted(results, key=results.get, reverse=True):
        print "{} -> {}".format(key, results[key])


def get_score(word):
    word = [c.lower() for c in word]
    return sum([scores[c] for c in word])


def is_winner(word, letters):
    rack = list(letters)
    for c in word:
        if c in rack:
            rack.remove(c)
        else:
            return False
    return True


def get_next_word():
    f = open('words.txt', 'r')
    for word in f:
        yield word.strip()

    f.close()

if __name__ == '__main__':
    start_time = time.time()
    findwords()
    print("--- %s seconds ---" % (time.time() - start_time))
