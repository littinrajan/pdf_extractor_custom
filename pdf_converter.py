# import python libraries
from pdf2image import convert_from_path
from os import path

def pdf_to_image_conversion(pdf_path):
    """
    Function to convert PDF pages to image
    :param pdf_path: path of source pdf file
    :return: file_name_list
    """
    # store pdf with convert_from_path function
    file_name_list = []
    images = convert_from_path(pdf_path)

    try:
        for n, image_n in enumerate(images):
            file_path = path.join('tmp', f'pdf_page_{n}.png')
            file_name_list.append(file_path)
            if image_n.mode != 'RGB':
                # RGB conversion
                rgb_image = image_n.convert('RGB')
            else:
                rgb_image = image_n
            # save pages as images in the destination folder
            rgb_image.save(file_path, 'PNG')
        print("PDF have converted to images by pages")
    except Warning:
        print('No images converted from the given PDF file')
        pass
    return file_name_list
