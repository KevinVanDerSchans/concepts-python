# Is it an anagram?

"""
Write a function that receives two words (String) and returns
true or false (Bool) depending on whether they are anagrams or not.

- An Anagram consists of forming a word by rearranging ALL of the letters of another
  the letters of another initial word.
- It is NOT necessary to check that both words exist.
- Two words that are exactly the same are not an anagram.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("listen", "silent")) # True
print(is_anagram("table", "fork")) # False
