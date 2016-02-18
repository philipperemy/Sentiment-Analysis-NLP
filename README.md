# Simple sentiment analysis examples 
Sentiment analysis applied to different datasets such as IMDB. The perceptron implementation uses [Keras](http://keras.io/), a minimalist, highly modular neural networks library, written in Python and capable of running on top of either TensorFlow or Theano.

## Documentation
What is [Sentiment Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Sentiment_analysis) ?  <br />
[Getting Started ](http://keras.io/#getting-started-30-seconds-to-keras) in 30 seconds with Keras.

## How to

```
git clone https://github.com/philipperemy/Sentiment-Analysis-NLP.git
cd Sentiment-Analysis-NLP
chmod +x init.sh
./init.sh
python main_perceptron.py
```

The script will download the [IMDB Sentiment Database](http://ai.stanford.edu/~amaas/data/sentiment/) from Stanford University and unzip it.

Also, we consider the list of positive and negative words from Illinois University, available [here](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon). This list has around 6800 words that we refer as keywords.
