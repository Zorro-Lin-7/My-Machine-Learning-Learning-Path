import sys

def wordfreq(mystring):
    """
    Function to generated the frequency distribution of the given text.
    """
    print(mystring)
    word_freq = {}
    for tok in mystring.split():
        if tok in word_freq:
            word_freq[tok] += 1
        else:
            word_freq[tok] = 1
    print(word_freq)
    
def main():
    str = "This is my first NLP program!"
    wordfreq(str)


if __name__ == '__main__':
    main()