# Reversing strings

"""
Create a program that reverses the order of a string of text
without using language functions that do it automatically.

- If we pass "Hello world" it would return "dlrow olleH".
"""


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hello world"))
