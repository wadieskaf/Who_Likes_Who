from string import punctuation
from collections import defaultdict

FILE_NAME = "sentences.txt"  # the name or location of the file that contains the sentences
FEELING_WORDS = {'likes', 'hates', 'loves'}  # Words that describe feelings
STOP_WORDS = {'and', 'but'}  # stop words in the sentences
feelings_database = defaultdict(lambda: defaultdict(list))  # storing data in a nested dictionary


# Function for finding the next feeling word
def find_next_feeling_word(word_list):
    try:
        index = next(idx for idx, w in enumerate(word_list) if w in FEELING_WORDS)
        return index
    except StopIteration:
        return None


def likes(name):
    names = feelings_database[name]['likes']
    if names == list():  # if the list is empty
        names.append('nobody')
    print(name + " likes %s" % ' and '.join(names))


def hates(name):
    names = feelings_database[name]['hates']
    if names == list():  # if the list is empty
        names.append('nobody')
    print(name + " hates %s" % ' and '.join(names))


def loves(name):
    names = feelings_database[name]['loves']
    if names == list():  # if the list is empty
        names.append('nobody')
    print(name + " loves %s" % ' and '.join(names))


with open(FILE_NAME) as f:
    sentences = f.readlines()
# reading the file row by row
for sentence in sentences:
    # splitting the sentence into words
    sentence_words = sentence.split()
    # Counting the words
    sentence_words_count = len(sentence_words)
    # The first word is always the name of the person who has the feelings
    name = sentence_words[0]
    index = 1
    while True:
        # The word after the person's name is always the feeling he has
        feeling = sentence_words[index].strip(punctuation)
        # find the index og the next feeling word
        next_feeling_word_index = find_next_feeling_word(sentence_words[index + 1:])
        # if this was the last feeling word in the sentence we add all the names after it and then break
        if next_feeling_word_index is None:
            for word in sentence_words[index: sentence_words_count]:
                word = word.strip(punctuation)
                if word not in STOP_WORDS:
                    feelings_database[name][feeling].append(word)
            break
        # If this was not the last feeling words
        else:
            # Add the index to the result of the function that found the index in the sliced list in order to get the
            # corresponding index in the original list
            next_feeling_word_index += index + 1
            # We slice all the words between the two feeling words
            sentence_slice = sentence_words[index + 1: next_feeling_word_index]
            for word in sentence_slice:
                # Get rid of punctuation
                word = word.strip(punctuation)
                # check for stop words
                if word not in STOP_WORDS:
                    # add the word to database
                    feelings_database[name][feeling].append(word)
            index = next_feeling_word_index

# Showing the results
likes('Jim')
hates('Bob')
loves('Larry')
