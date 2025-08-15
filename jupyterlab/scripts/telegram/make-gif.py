import os

# List all files and directories in the current directory
files = os.listdir('.')  # '.' means current directory

# Filter out only files (excluding directories)
files_only = [f for f in os.listdir('./custom_folder')]

print(len(files_only))

files = files_only  # your full list here

# Sort by the numeric prefix (before '_')
sorted_by_number = sorted(files, key=lambda x: int(x.split('_')[0]), reverse=True)

print("Sorted by number:")
print(sorted_by_number[88:115])  # print first 5 as example

from PIL import Image

# Take list of paths for images
image_path_list = sorted_by_number

# Create a list of image objects
image_list = [Image.open(f"./custom_folder/{file}") for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=100, # in milliseconds
            loop=0)

