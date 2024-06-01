import cv2
import numpy as np
import pytesseract


def draw_text_boxes(image_bytes, identified_texts, display_img=False):
    """
    Draw bounding boxes around identified texts in an image.
    This function takes image bytes and a list of identified texts as input,
    converts the image bytes to a numpy array, uses Tesseract OCR to detect
    text in the image, and draws bounding boxes around the identified texts.
    It returns a list of box coordinates.
    Args:
        image_bytes (bytes): Image bytes to process.
        identified_texts (list): A list of texts to identify and draw bounding
            boxes around.
        display_img (bool, optional): Whether to display the image with bounding
            boxes. Defaults to False.
    Returns:
        list: A list of tuples containing box coordinates (x, y, width, height).

    """
    # Convert image bytes to a numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    box_coordinates = []

    # Iterate through each word detected
    for i in range(len(data['text'])):
        text = data['text'][i]
        if text in identified_texts:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            box_coordinates.append((x, y, w, h))

    if display_img:
        # Display the image with bounding boxes
        cv2.imshow('Identified Text Boxes', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return box_coordinates