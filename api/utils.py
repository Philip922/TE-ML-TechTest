import base64

def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    return base64_encoded


def decode_base64_to_image(base64_string: str) -> bytes:
    try:
        # Decode base64 string to bytes
        image_bytes = base64.b64decode(base64_string)
        return image_bytes
    except Exception as e:
        # Handle exceptions such as invalid base64 string
        print(f"Error decoding base64 string: {e}")
        return b""


from PIL import Image
import io

def print_jpg_image(image_bytes: bytes):
    try:
        # Load image from bytes
        image = Image.open(io.BytesIO(image_bytes))
        # Display image
        image.show()
        print('ffgghgh')
    except Exception as e:
        # Handle exceptions such as invalid image bytes
        print(f"Error displaying image: {e}")


impath = "/home/philip/Documents/Develop/Tenant/TE-ML-TechTest/examples/samples/JuneM.jpg"
enc = encode_image_to_base64(impath)
print(enc)