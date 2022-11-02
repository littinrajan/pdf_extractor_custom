from PIL import Image
from pytesseract import pytesseract

def extract_text(image_list):
    """
    Function to extract the text from converted images
    :param image_list: list of images with path
    :return: text_data
    """
    # initializing text data
    text_data = ""
    # iterating over the images and performing extraction
    for image_n in image_list:
        img = Image.open(image_n)
        text = pytesseract.image_to_string(img)
        text_data += "\n\n" + text
    return text_data
