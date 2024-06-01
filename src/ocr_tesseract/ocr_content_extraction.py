"""
Utility functions for image and text processing.

This module provides various utility functions for converting PDF files to images,
extracting image bytes, cleaning extracted text, and performing OCR (Optical
Character Recognition) content extraction using Tesseract.

Functions:
- convert_pdf_to_images: Convert PDF files to a list of image byte arrays.
- extract_image_bytes: Extract image bytes from a list of image file paths.
- clean_text: Clean extracted text by removing empty lines and extra spaces.
- extract_text_with_pytesseract: Extract text from images using Tesseract OCR.
- ocr_content_extraction: Perform OCR content extraction from a list of files.
"""

import os
import io
import pytesseract
import pypdfium2 as pdfium
from io import BytesIO
from PIL import Image, ImageOps

def convert_pdf_to_images(file_path, scale=300 / 72):
    pdf_file = pdfium.PdfDocument(file_path)
    page_indices = [i for i in range(len(pdf_file))]
    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices=page_indices,
        scale=scale,
    )
    list_final_images = []
    for i, image in zip(page_indices, renderer):
        image_byte_array = BytesIO()
        image.save(image_byte_array, format='jpeg', optimize=True)
        image_byte_array = image_byte_array.getvalue()
        list_final_images.append(dict({i: image_byte_array}))
    return list_final_images


def extract_image_bytes(file_paths):
    list_final_images = []

    for i, file_path in enumerate(file_paths):
        if os.path.isfile(file_path):  # Check if the path is a file
            try:
                with open(file_path, 'rb') as image_file:
                    image_byte_array = io.BytesIO(image_file.read())
                    image_bytes = image_byte_array.getvalue()
                    # Convert the image bytes to a PIL Image
                    image = Image.open(io.BytesIO(image_bytes))
                    # Convert the image to JPEG format
                    jpeg_byte_array = io.BytesIO()
                    image.convert('RGB').save(jpeg_byte_array, format='JPEG')
                    jpeg_bytes = jpeg_byte_array.getvalue()
                    # Append the JPEG bytes to the final list
                    list_final_images.append({i: jpeg_bytes})
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        else:
            print(f"Path is not a file: {file_path}")
    return list_final_images


def clean_text(text):
    """
    Cleans the extracted text by removing empty lines and extra spaces.
    Args:
    text (str): The extracted text from an image
    Returns:
    str: The cleaned text.
    """
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text


def extract_text_with_pytesseract(list_dict_final_images):
    #TODO: Handle rotated images
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []
    for index, image_bytes in enumerate(image_list):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            # Correct the orientation based on EXIF data
            image = ImageOps.exif_transpose(image)
            raw_text = pytesseract.image_to_string(image)
            image_content.append(raw_text)
        except Exception as e:
            print(f"Error processing image at index {index}: {e}")
    return "\n".join(image_content)


def ocr_content_extraction(files_path:list)->list:
    image_data = []
    for file_path in files_path:
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_data.extend(extract_image_bytes([file_path]))
        elif file_path.lower().endswith('.pdf'):
            image_data.extend(convert_pdf_to_images(file_path))
    text_with_pytesseract = extract_text_with_pytesseract(image_data)
    clean_extraction = clean_text(text_with_pytesseract)
    return clean_extraction