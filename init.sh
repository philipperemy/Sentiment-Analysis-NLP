#!/usr/bin/env bash
wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
echo "Successfully downloaded the IMDB database."
tar xvzf aclImdb_v1.tar.gz
rm -f aclImdb_v1.tar.gz
wget http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar
unrar e opinion-lexicon-English.rar
rm -f opinion-lexicon-English.rar
