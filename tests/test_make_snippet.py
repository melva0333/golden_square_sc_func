# A function called make_snippet that takes a string 
# as an argument and returns the first five words 
# and then a '...' if there are more than that.
from lib.make_snippet import *

def test_given_a_string_returns_first_words():
    result = make_snippet("Hello, how are you today and what are you upto?")
    assert result == "Hello, how are you today..."

def test_given_a_string_returns_first_words_2():
    result = make_snippet("J'meappelle Selva, je suis content! Et vous?")
    assert result == "J'meappelle Selva, je suis content!..."