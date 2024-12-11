import os
import logging
from PIL import Image, ImageOps, ImageFilter
from glob import glob  # for finding all images in a directory

# Configure logging
logging.basicConfig(filename='image_processing.log', level=logging.INFO)

# Function to check if a file is a valid image
def is_valid_image(filepath):
    if not os.path.isfile(filepath):
        logging.warning(f"File not found: {filepath}")
        return False
    _, ext = os.path.splitext(filepath)
    return ext.lower() in ('.png', '.jpg', '.jpeg')

# Function to process the image
def process_image(filepath):
    try:
        img = Image.open(filepath).convert("RGBA")
        inverted_img = ImageOps.invert(img.convert("RGB")).convert("RGBA")

        data = inverted_img.getdata()
        new_data = []
        for item in data:
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append((255, 255, 255, item[3]))
        inverted_img.putdata(new_data)

        sharpened_img = inverted_img.filter(ImageFilter.UnsharpMask(radius=2, percent=300, threshold=3))
        sharpened_img = sharpened_img.filter(ImageFilter.UnsharpMask(radius=2, percent=300, threshold=3))

        filename = os.path.basename(filepath)
        output_path = os.path.join(output_directory, "processed_" + filename)
        sharpened_img.save(output_path, 'PNG', quality=95)

        logging.info(f"Successfully processed image: {filepath}")
        return output_path
    except Exception as e:
        logging.error(f"Error processing image: {filepath} - {e}")
        return None

# Get user input for image directory or use a default path
image_dir = input("Enter directory containing images (or leave blank for default): ") or "/Users/yashovardhn/Downloads/"

# Find all image files in the directory
image_paths = glob(os.path.join(image_dir, "*.+(png|jpg|jpeg)"))

# Define the output directory
output_directory = "/Users/yashovardhn/Documents/PWC Adworks"

# Process each image and save the results
output_paths = []
for path in image_paths:
    if is_valid_image(path):
        output_path = process_image(path)
        if output_path:
            output_paths.append(output_path)

print(f"Processed images saved to: {output_directory}")
