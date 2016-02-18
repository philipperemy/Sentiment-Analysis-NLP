# Simple sentiment analysis examples 
Sentiment analysis applied to different datasets such as IMDB. The perceptron implementation uses [Keras](http://keras.io/), a minimalist, highly modular neural networks library, written in Python and capable of running on top of either TensorFlow or Theano.

## Documentation
What is [Sentiment Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Sentiment_analysis) ?  <br />
Learn in 30 seconds with [Keras](http://keras.io/#getting-started-30-seconds-to-keras).

## Getting Started
```
git clone https://github.com/philipperemy/Sentiment-Analysis-NLP.git
cd Sentiment-Analysis-NLP
chmod +x init.sh
./init.sh
python main_perceptron.py
```

The script will download the [IMDB Sentiment Database](http://ai.stanford.edu/~amaas/data/sentiment/) from Stanford University and unzip it.

Also, we consider the list of positive and negative words from Illinois University, available [here](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon). This list has around 6800 words that we refer as keywords.

## Execution

You should have a console output similar to the one below.

```
Using TensorFlow backend.
=> loaded 2006 positive words
=> loaded 4783 negative words
=> processed 500 aclImdb/train/neg files.
[...]
=> processed 5000 aclImdb/train/neg files.
=> processed 500 aclImdb/train/pos files.
[...]
=> processed 5000 aclImdb/train/pos files.
I tensorflow/core/common_runtime/local_device.cc:40] Local device intra op parallelism threads: 4
I tensorflow/core/common_runtime/direct_session.cc:58] Direct session inter op parallelism threads: 4
Epoch 1/200
6666/6666 [==============================] - 22s - loss: 0.2177    
[...]  
```

## Results

On 10k reviews with 2/3 training and 1/3 validation set (200 epochs). <br />
```
training= 0.803180318032
validation= 0.732913669065
```
