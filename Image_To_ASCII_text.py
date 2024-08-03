import pywhatkit

pywhatkit.image_to_ascii_art("C:/Users/harsh/Desktop/Python_Projects/Image.jpg","ascii.txt")

import ascii_magic

output=ascii_magic.from_image("C:/Users/harsh/Desktop/Python_Projects/Image.jpg")

output.to_terminal(columns=100,char="#")
