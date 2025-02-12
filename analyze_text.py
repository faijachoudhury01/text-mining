import urllib.request 
import string



def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

    
def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)
    
    

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace('—', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1
            

    return hist
    


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""
    # Since we already created the list of words with their count. We can just count length of the list to find the difference of the words
    return len(hist)

def most_common (hist, excluding_stopwords= True):
    ''' Find most common word of the text, excluding the stop words (is, are, the , and)'''

    l= []

    stop_words = process_file ('data/stop words.txt', False)
    #print (stop_words)  to test   
    stop_words = list(stop_words.keys())
    #print (stop_words)

    for word, frequency in hist.items(): # we need both the words and the frequency of the word to see which one have the most count
        if excluding_stopwords:
            if word in stop_words:
                continue

        l.append((word, frequency))

    l.sort(reverse=True)
    return l


def print_most_common(hist, num=10):
    """Prints the most commons words  using the function 'most_common'
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def main():
    # url = 'https://www.gutenberg.org/files/25344/25344-0.txt'
    # response = urllib.request.urlopen(url)
    # data = response.read() 
    # text = data.decode('utf-8')
    # print (text) # to test

    # line 77 to 81 are for when you want to dowland the file from online

    hist = process_file('data/Scarlet Letter.txt', skip_header=True)
    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    l = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in l[:100]:
        print(word, '\t', freq)

    # words = process_file('words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
