#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image
import os

def get_image_sizes(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg')):
            try:
                img_path = os.path.join(folder_path, filename)
                with Image.open(img_path) as img:
                    width, height = img.size
                    print(f"{filename}: {width}px:{height}px")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage:
folder_path = "./custom_folder"  # Replace with your folder path
get_image_sizes(folder_path)


# In[8]:


from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(1280, 1280)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                img_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                with Image.open(img_path) as img:
                    # Resize while maintaining aspect ratio (thumbnail method)
                    img.thumbnail(target_size, Image.Resampling.LANCZOS)
                    
                    # Create a new blank image (1280x1280) with white background
                    new_img = Image.new("RGB", target_size, (255, 255, 255))
                    
                    # Paste the resized image centered on the blank canvas
                    new_img.paste(
                        img,
                        (
                            (target_size[0] - img.width) // 2,  # Center X
                            (target_size[1] - img.height) // 2  # Center Y
                        )
                    )
                    
                    new_img.save(output_path)
                    print(f"Resized {filename} → 1280px:1280px")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage:
input_folder = "./custom_folder"  # Folder containing original images
output_folder = "./resized_custom_folder"  # Folder to save resized images
resize_images(input_folder, output_folder)


# In[9]:


import os

# List all files and directories in the current directory
files = os.listdir('.')  # '.' means current directory

# Filter out only files (excluding directories)
files_only = [f for f in os.listdir('./resized_custom_folder')]

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
image_list = [Image.open(f"./resized_custom_folder/{file}") for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation-2.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=100, # in milliseconds
            loop=0)


# In[ ]:




