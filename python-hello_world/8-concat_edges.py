#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join([str[39:39+27], str.split(" ")[12], str.split(" ")[0]])
print(str)
