#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Part 1 Result 1 Count Words in a String - Counts the number of individual words in a string. 
# For added complexity read these strings in from a text file and generate a summary.
def count_words(text):
    return str(len(text.split(" "))) + " words in the analyzed text" 

def count_from_file(file_location):
    with open(file_location, 'r') as file:  # Use 'with' to open the file
        text = file.read()  # No need to cast to str, read() already returns a string
    return count_words(text)

# Corrected print statements
print(count_words("This is a sentence with 7 words"))
print(count_from_file("myfile.txt"))

