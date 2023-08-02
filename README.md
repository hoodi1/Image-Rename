# Image Renaming Tool

This script is a simple Python tool that extracts metadata from image files and renames them based on user-defined patterns. The tool utilizes the `os`, `exifread`, and `re` modules to achieve this functionality.

## Prerequisites

Before running the script, ensure you have Python installed on your system. The script was tested on Python 3. If you don't have Python installed, you can download it from the official website: [Python.org](https://www.python.org/).

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the `rename_images.py` script.

## Usage

1. Open your terminal or command prompt.
2. Run the script using the following command:

```bash
python rename_images.py
```

3. The script will prompt you for the input directory path, output directory path, and renaming pattern.

### Input Directory Path

Enter the full path of the directory containing the images you want to rename.

### Output Directory Path

Enter the full path of the directory where you want to save the renamed images. If the directory does not exist, the script will create it for you.

### Renaming Pattern

Enter a pattern for renaming the images. You can use the following placeholders in the pattern:

- `{date_time}`: Replaced with the image's original DateTime metadata or "Unknown_DateTime" if unavailable.
- `{camera_model}`: Replaced with the image's camera model metadata or "Unknown_Model" if unavailable.
- `{location}`: Replaced with the image's GPS latitude metadata or "Unknown_Location" if unavailable.

If you don't provide a renaming pattern, the script will use the default pattern: "{date_time} {camera_model}.jpeg".

## Example

Let's consider an example usage:

- Input Directory: `/path/to/input_directory`
- Output Directory: `/path/to/output_directory`
- Renaming Pattern: `{date_time}_{location}_{camera_model}.jpg`

The script will process all the image files (with extensions .jpg, .jpeg, .png, .gif) in the `input_directory`, extract the relevant metadata, create the new filenames based on the provided pattern, remove any invalid characters, and save the renamed images to the `output_directory`.

## Note

- The script uses the `exifread` module to extract metadata from the images. Ensure you have it installed. If not, you can install it using pip:

```bash
pip install exifread
```

- The script will overwrite existing files in the output directory if they have the same name as the newly generated filenames.

- It is recommended to make a backup of your images before running the script.
