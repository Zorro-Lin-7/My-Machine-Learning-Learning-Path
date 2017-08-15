import nltk
from nltk.stem import WordNetLemmatizer


class Splitter(object):
    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
        
    def split(self, text):
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences
        
class PosTagger(object):
    def __init__(self):
        pass
    
    def pos_tag(self, sentences):
        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        pos = [[(word, WordNetLemmatizer().lemmatize(word), [postag]) for (word, postag) in sentence] for sentence in pos]
        
        return pos
 
       
if __name__ == "__main__":
    text = """
        Why are you looking disappointed. We will go to restaurant for dinner.
        """
    splitter = Splitter()
    postagger = PosTagger()
    splitted_sentences = splitter.split(text)
    print(splitted_sentences)
    
    pos_tagged_sentence = postagger.pos_tag(splitted_sentences)
    print(pos_tagged_sentence)
    