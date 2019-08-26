import re, string
import src.vendor.snowball.stemmer as Stemmer


class StemWordsOperation:
    def get(self, text):
        text = text.lower().replace("ё", "е")
        text = re.sub('([1-9])', 'NUMBER', text)
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
        text = re.sub('@[^\s]+', 'USER', text)
        text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
        text = re.sub(' +', ' ', text)
        word_list = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
        stem = Stemmer.Stemmer()
        for i in range(len(word_list)):
            word_list[i] = stem.stem(word_list[i])
        return word_list
