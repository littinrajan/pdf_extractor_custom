# import required libraries
import re

def filter_text(text_data):
    """
    Function to pre-process the text data
    :param text_data: input text data
    :return: text_data
    """
    # punctuations to be removed
    FILTER_PUNCTUATIONS = '''!()[]{};'"\|,‘<>“?@#$%^&+*_~'''
    # remove unwanted lines
    text_data = "\n".join([line.strip() for line in text_data.strip().split('\n')])
    # removing awful character
    text_data = re.sub(r"\x0c", "\n", text_data)
    # replacing newlines with more than 3 consecutive occurrences with '\n\n'
    text_data = re.sub(r"\n{3,}", "\n\n", text_data)
    # removing unwanted punctuations from the text
    text_data = text_data.translate(str.maketrans('', '', FILTER_PUNCTUATIONS))
    # replacing spaces with more than 2 consecutive occurrences with ' '
    text_data = re.sub(r" {2,}", " ", text_data)
    return text_data
