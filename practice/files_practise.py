f = open (r"C:\Users\sreed\OneDrive\Desktop\raju.txt","r")
ab = f.readlines()
for i in ab:
    if 'sekhar' not in  i:
       print(i)
       continue

print(ab)

f = open(r"C:\Users\sreed\OneDrive\Desktop\raju.txt","w")
f.write("ramu")
b = f.write(str())


