# Book2Audio
# Search, project gutenberg for public domain books and convert them to Audiobooks
# Written by Shane Aldridge on PyCharm using Python310
# A CSV of all books on project gutenberg can be found here
# https://www.gutenberg.org/ebooks/offline_catalogs.html#affiliate-sites

import winsound
import pandas as pd
import requests
from gtts import gTTS
import ffmpeg

# <------------get book by user submitted title---------------->

# Get user input
title = input("Enter title name; ")

# read project gutenberg csv file
print("The title you selected is: " + title)
df = pd.read_csv("pg_catalog.csv", low_memory=False)

# filtering the rows where input = title
if df['Title'].str.contains(title).any():
    print(df.loc[df['Title'].str.contains(title)])
else:
    print("No titles found. Please check your spelling and capitalization!")
    exit()

# Select the text number coresponding to the title you want
dn = input('Type the text# for your book: ')

# Concatenate web address with text number
webbook = ('https://www.gutenberg.org/cache/epub/' + dn + '/pg' + dn + '.txt')
# print out the string for the text number
print(webbook)
# open the webpage
response = requests.get(webbook)
# Save text as a variable
text0 = (response.text)
# Print out full text
print(text0)

# remove intro statement
sep = "*** START OF THE PROJECT GUTENBERG EBOOK"
text1 = text0.split(sep, 1)[1]
print(text1)

# Remove outro statement
sep = "*** END OF THE PROJECT GUTENBERG EBOOK"
text2 = text1.split(sep, 1)[0]
print(text2)

try:
    # Save the output as a text file
    # Open the file
    text_file = open("text2.txt", 'w', encoding="utf-8")
    # Write the text
    text_file.write(text2)
    # Close the file
    text_file.close()
    #Closes the .txt file#
    print("UTF-8 encoding")

# <------------------------Use TTS engine to save as an audio file ----------------------->

    # open the file to read
    fh = open("text2.txt", "r")
    # Replace lines with spaces
    fintext = fh.read().replace("\n", " ")
    # select what language to read the text in
    l = input("Select output language: en for English, fr for French, sp for Spanish ")
    # Define reading parameters
    output = gTTS(text=fintext, lang=l, slow=False)
    # Save the file
    output.save(title + ".mp3")
    # Close the document
    fh.close()
except:
    # Open the file
    text_file = open("text2.txt", 'w', encoding="utf-16")
    # Write the text
    text_file.write(text2)
    # Close the file
    text_file.close()
    #Closes the .txt file#
    print("UTF-16 encoding")

    # open the file to read
    fh = open("text2.txt", "r")
    # Replace lines with spaces
    fintext = fh.read().replace("\n", " ")
    # select what language to read the text in
    l = input("Select output language: en for English, fr for French, sp for Spanish ")
    # Define reading parameters
    output = gTTS(text=fintext, lang=l, slow=False)
    # Save the file
    output.save(title + ".mp3")
    # Close the document
    fh.close()

# <-----------------------Convert mp3 to other formats--------------------------------->

# Play a sound when done
winsound.Beep(700, 200)
