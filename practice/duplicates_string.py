

## initializing string
string = "welcome to america"
## initializing a list to append all the duplicate characters
duplicates = []
for i in string:
   ## checking whether the character have a duplicate or not
   ## str.count(char) returns the frequency of a char in the str
   if string.count(i) > 1:
   ## appending to the list if it's already not present
     if i not in duplicates:
       duplicates.append(i)
print(duplicates)
 