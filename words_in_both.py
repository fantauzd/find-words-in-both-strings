# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 8/3/2023
# Description: takes two strings as parameters and returns
# a set of only those words that appear in both strings. Returns the set in all lowercase.

def words_in_both(string_a, string_b):
    """
     takes two strings as parameters and returns a set of only those words that appear in both strings
    :param string_a: string
    :param string_b: string
    :return: set of common words
    """
    lower_list_a = string_a.lower().split()  # Changes the string to a list of words
    lower_list_b = string_b.lower().split()
    result = set()  # Initializes an empty set
    for word in lower_list_a:  # Iterates for each word in string_a
        if word in lower_list_b:  # Finds words that are also in string_b
            result.add(word)  # Adds common word to set
    return result
