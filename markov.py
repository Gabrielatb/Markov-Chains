"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    data = open(file_path)
    content = data.read()

    return content
    data.close()

# print open_and_read_file('gettysburg.txt')


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

    for index in range(len(words_list)-n):
        key = (words_list[index], words_list[index + 1])
        value = words_list[index + n]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains


def make_text(chains):
    """Return text from chains."""
    #print chains

    words = []
    new_key = choice(chains.keys())
    #value = choice(chains[new_key])
    words.extend(new_key)
    #words.append(value)
    #chains[("I", "am?")] = None

    while new_key in chains:
        value = choice(chains[new_key])
        words.append(value)
        new_key = (new_key[1], value)   

    return " ".join(words)


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
print argv[1]
print argv[2], argv[1]
