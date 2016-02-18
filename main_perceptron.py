import utils
import numpy as np
import os
from perceptron.perceptron_model import get_model
from random import shuffle

from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD


def get_model(X, y):
    model = Sequential()
    model.add(Dense(1, input_dim=X.shape[1]))
    model.add(Activation('sigmoid'))
    sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    model.fit(X, y, nb_epoch=200, batch_size=1)
    return model


def process_words(cur_file, input_nn):
    words = utils.read_words_from_file(cur_file)
    positive_count = 0
    negative_count = 0
    inputs = np.zeros(len(all_words))
    for word in words:
        if word in positive_words:
            positive_count += 1
            idx = all_words.index(word)
            inputs[idx] += 1
        elif word in negative_words:
            negative_count += 1
            idx = all_words.index(word)
            inputs[idx] += 0
    input_nn.append(inputs)


def load_inputs(folder, label, count, input_nn):
    file_count = 0
    for cur_file in os.listdir(folder):
        if cur_file.endswith(".txt"):
            process_words(folder + "/" + cur_file, input_nn)
            targets.append(label)
            file_count += 1
            if file_count % (count/10) == 0:
                print "=> processed", file_count, folder, "files."

            if file_count > count:
                break

if __name__ == '__main__':

    positive_words = utils.get_positive_words()
    negative_words = utils.get_negative_words()

    all_words = positive_words + negative_words

    print "=> loaded", len(positive_words), "positive words"
    print "=> loaded", len(negative_words), "negative words"

    input_nn = []
    targets = []

    samples_per_category = 5000
    load_inputs("neg", 0, samples_per_category, input_nn)
    load_inputs("pos", 1, samples_per_category, input_nn)

    input_nn_shuffle = []
    targets_shuffle = []
    index_shuffle = range(len(input_nn))
    shuffle(index_shuffle)
    for i in index_shuffle:
        input_nn_shuffle.append(input_nn[i])
        targets_shuffle.append(targets[i])

    num_categories = 2
    cutoff = int(float(samples_per_category * num_categories) * 2 / 3)
    input_nn_shuffle = np.array(input_nn_shuffle)
    targets_shuffle = np.array(targets_shuffle)

    input_nn_train = input_nn_shuffle[:cutoff]
    targets_train = targets_shuffle[:cutoff]

    input_nn_valid = input_nn_shuffle[cutoff:]
    targets_valid = targets_shuffle[cutoff:]

    model = get_model(input_nn_train, targets_train)

    predict_train = model.predict(input_nn_train) > 0.5
    print "training=", np.mean(np.array(predict_train[:, 0], dtype=int) == targets_train)

    predict_valid = model.predict(input_nn_valid) > 0.5
    print "validation=", np.mean(np.array(predict_valid[:, 0], dtype=int) == targets_valid)

