from sys import argv

from pip._vendor.distlib.compat import raw_input

script, filename = argv

txt = open(filename)

print("Here's your file %s" %filename)
print(txt.read())

print("Type the file again:")
file_again = raw_input(">")

txt_again = open(file_again)

print(txt_again.read())


