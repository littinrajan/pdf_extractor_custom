# import required libraries
from os import path
import json
from pdf_converter import pdf_to_image_conversion
from data_extractor import extract_text
from data_filter import filter_text
from entity_extractor import extract_entities

def pdf_entity_extraction(pdf_path):
    """
    Function to Extract entities from PDF
    :param pdf_path:
    :return:
    """
    # extract pdf pages to images
    image_files = pdf_to_image_conversion(pdf_path)
    # get extracted text from each page
    extracted_text = extract_text(image_files)
    # filter text data for better entity parsing
    filtered_text = filter_text(extracted_text)
    # parse entities from text data
    extracted_data = extract_entities(filtered_text)
    # save extracted entity dictionary as json data
    with open(path.join('result', "pdf_entities.json"), "w") as json_obj:
        json.dump(extracted_data, json_obj)
    print(">> Entity Extraction completed")


if __name__ == '__main__':
    pdf_file_path = path.join('data', 'Aventus ML Machine test.pdf')
    pdf_entity_extraction(pdf_file_path)
