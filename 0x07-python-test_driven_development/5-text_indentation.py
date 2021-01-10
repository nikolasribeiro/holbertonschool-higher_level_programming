#!/usr/bin/python3

""" 
Text Identantio
"""


def text_indentation(text):
    """ Text identation function """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ Check if the text contains any of this characters and replace it with 2 new lines
    """
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")

    for line in range(0, len(text)):
        print("{}".format(text[line].strip()), end=(
            "" if (line == len(text) - 1) else "\n"))
