import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from src.ocr_tesseract.ocr_box_coordinates import draw_text_boxes

image_path = os.path.join(project_root, 'examples', 'samples', 'JuneM.jpg')
identified_text = ['JUNE', 'MARIE']

# Read image
with open(image_path, 'rb') as f:
    image_bytes = f.read()

out = draw_text_boxes(image_bytes, identified_text, display_img=True)
print(out)