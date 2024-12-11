from PIL import Image, ImageOps
import os

# File paths for the uploaded images
file_paths = [
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (12).png", 
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (17).png", 
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (15).png", 
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (16).png", 
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (14).png", 
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (13).png",
    "/Users/yashovardhn/Downloads/300x300 (300 x 300 px) (11).png",
]

# Directory to save processed images
output_directory = "/Users/yashovardhn/Documents/PWC Adworks/"

# Function to convert the image to white logos on transparent background
def process_image(file_path):
    # Open the image
    img = Image.open(file_path).convert("RGBA")
    
    # Invert image to make the content white
    inverted_img = ImageOps.invert(img.convert("RGB"))
    inverted_img = inverted_img.convert("RGBA")
    
    # Make the background transparent
    data = inverted_img.getdata()
    new_data = []
    for item in data:
        if item[:3] == (255, 255, 255):  # Check for white areas
            new_data.append((255, 255, 255, 0))  # Make them transparent
        else:
            new_data.append((255, 255, 255, item[3]))  # Keep original transparency
    inverted_img.putdata(new_data)
    
    # Save the processed image to the specified directory
    filename = os.path.basename(file_path)
    output_path = os.path.join(output_directory, "processed_" + filename)
    inverted_img.save(output_path, 'PNG', quality=95)
    
    return inverted_img

# Process each image and save the results
output_paths = []
for i, path in enumerate(file_paths):
    output_path = process_image(path)
    output_paths.append(output_path)

output_paths
