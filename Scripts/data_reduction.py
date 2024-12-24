"""
Created on Tue Dec 10 19:48:22 2024

@author: Shourish Kothawale

Title: Data Reduction

"""

import os

def delete_files_after_300(main_folder_path):
    """
    Deletes files after the first 300 images in each subfolder of a given main folder.

    Args:
        main_folder_path (str): Path to the main folder containing subfolders.
    """
    for subfolder_name in os.listdir(main_folder_path):
        subfolder_path = os.path.join(main_folder_path, subfolder_name)
        
        # Ensure it's a directory
        if os.path.isdir(subfolder_path):
            # Get a list of all image files in the subfolder
            image_files = [
                f for f in os.listdir(subfolder_path)
                if os.path.isfile(os.path.join(subfolder_path, f)) and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
            ]

            # Sort files to ensure consistent order
            image_files.sort()

            # If more than 300 images, delete the extra ones
            if len(image_files) > 300:
                for extra_file in image_files[300:]:
                    file_to_delete = os.path.join(subfolder_path, extra_file)
                    os.remove(file_to_delete)
                    print(f"Deleted: {file_to_delete}")

# Example usage
main_folder_path = "..\\Data"
delete_files_after_300(main_folder_path)