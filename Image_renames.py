import os
import exifread
import re

def extract_metadata(image_path):
    # Open the image file and extract metadata using exifread
    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file)
    
    return tags         # this returns a dictionary which is stored in tags

def removeChar(filename):
    # Susbs any invalid characters with no space from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def renameImg(image_path, output_dir, renaming_pattern):
    # Extract metadata from the image file
    metadata = extract_metadata(image_path)

    # Get the relevant metadata fields (provide default values if metadata is missing)
    date_time = metadata.get('EXIF DateTimeOriginal', 'Unknown_DateTime')
    camera_model = metadata.get('Image Model', 'Unknown_Model')
    location = metadata.get('GPS GPSLatitude', 'Unknown_Location')

    # Create the new filename using the specified pattern
    new_filename = renaming_pattern.format(date_time=date_time,
                                           camera_model=camera_model,
                                           location=location)
    
    # remove any invalid characters
    new_filename = removeChar(new_filename)

    # Join the output directory path and the new filename
    new_image_path = os.path.join(output_dir, new_filename)

    # Rename the image file
    os.rename(image_path, new_image_path)

def renameImageInDir(input_dir, output_dir, renaming_pattern):
    # Loop through all image files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(input_dir, filename)
            renameImg(image_path, output_dir, renaming_pattern)

if __name__ == "__main__":
    # Get input and output directories from the user
    input_directory = input("Enter the input directory path: ")
    output_directory = input("Enter the output directory path: ")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the renaming pattern from the user or set a default pattern
    renaming_pattern = input("Enter the renaming pattern (use {date_time}, {camera_model}, {location}): ")
    if not renaming_pattern:
        renaming_pattern = "{date_time} {camera_model}.jpeg"

    # Call the renameImageInDir function
    renameImageInDir(input_directory, output_directory, renaming_pattern)

    print("Image renaming complete!")