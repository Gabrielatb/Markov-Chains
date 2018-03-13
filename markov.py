"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    data = open(file_path)
    content = data.read()

    return content
    data.close()

print open_and_read_file('green-eggs.txt')


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words_string = text_string.strip()
    words_list = words_string.split()

    for index in range(len(words_list)-2):
        key = (words_list[index], words_list[index + 1])
        value = words_list[index + 2]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains


def make_text(chains):
    """Return text from chains."""

    # words = []
    for key, value in chains.items():
         return key, value
    print words.append(value)

    # add each word to a list 
    # container = words 
    # link(new key) = the second word in tuple key (at random) and random value word
    # chains.choice(key)
    #take key[1] and make key[0] in new key and value becomes new key[1]
    #tuple[1], tuple[2], value
    #choose first tuple 
    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
