
from collections import Counter

def find_duplicates(s):
    elements = Counter(s)
    return [k for k,v in elements.items() if v>1]

print(find_duplicates("Hello"))

print(find_duplicates("Hippopotamus"))

print(find_duplicates("Python"))
