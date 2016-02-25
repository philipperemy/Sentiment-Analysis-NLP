def get_positive_words():
    positive_words = []
    with open("positive-words.txt") as f:
        for line in f:
            string = line[:-1]
            if len(string) > 0 and ";" not in string:
                positive_words.append(string)
    return positive_words


def get_negative_words():
    negative_words = []
    with open("negative-words.txt") as f:
        for line in f:
            string = line[:-1]
            if len(string) > 0 and ";" not in string:
                negative_words.append(string)
    return negative_words


def read_words_from_file(filename):
    input_str = ""
    with open(filename) as f:
        input_str += "".join(f.readlines()).replace("\n", " ")
    words = input_str.lower().split()
    return words
