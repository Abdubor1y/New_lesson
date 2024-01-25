#RegEx
import re

pattern = re.compile("[A-Z]+$") #Only uppercase letter

print(pattern.search("thisISMYPROJECT"))
