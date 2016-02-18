
def get_positive_words():
    positive_words = []
    with open("data/positive-words.txt") as f:
        for line in f:
            str = line[:-1]
            if len(str) > 0 and ";" not in str:
                positive_words.append(str)
    return positive_words


def get_negative_words():
    negative_words = []
    with open("data/negative-words.txt") as f:
        for line in f:
            str = line[:-1]
            if len(str) > 0 and ";" not in str:
                negative_words.append(str)
    return negative_words


def read_words_from_file(filename):
    input_str = ""
    with open(filename) as f:
        input_str += "".join(f.readlines()).replace("\n", " ")
    words = input_str.lower().split()
    return words