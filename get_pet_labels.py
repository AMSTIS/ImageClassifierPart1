#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Dr. Abdulla Mohammed Al Shimmari
# DATE CREATED:  26/11/2020                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
print("\nPrints 10 filenames from folder pet_images/")
for indexes in range(0, 10, 1):
    print("{:2d} file: {:>25}".format(indexes + 1, filename_list[indexes]))
    
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Determines number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    # a List that contains only one item - the pet image label

    for single_file in filename_list:
        # Sets pet_image variable to a filename 
        pet_label = ""
        pet_image = single_file

        # Sets string to lower case letters
        pet_image_lower_case = pet_image.lower()

        # Splits lower case string by _ to break into words 
        pet_image_splitted = pet_image_lower_case.split("_")

        # Create pet_name starting as empty string
        pet_name = ""

        # Loops to check if word in pet name is only
        # alphabetic characters - if true append word
        # to pet_name separated by trailing space 
        for word in pet_image_splitted:
            if word.isalpha():
                pet_name += word + " "

        # Strip off starting/trailing whitespace characters 
        pet_name = pet_name.strip()

        # Prints resulting pet_name
        print("\nFilename=", pet_image, " Label=", pet_name)

        if single_file not in results_dic:
            results_dic[single_file] = [pet_name]
        else:
            print("Warning Duplcate pet imge exists")
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
