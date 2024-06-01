import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from src.ocr_tesseract.ocr_content_extraction import ocr_content_extraction

samples_folder = os.path.join(project_root, 'examples', 'samples')
file_names = os.listdir(samples_folder)
for file_name in file_names:
    print(file_name)
    files_path = [os.path.join(samples_folder, file_name)]
    extracted_text = ocr_content_extraction(files_path)
    print(extracted_text)
    print('-'*30)
