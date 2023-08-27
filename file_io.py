import os

path = "C:\\Users\\ashwa\\Desktop\\python documents\\test.txt"

if os.path.exists(path):
    print("location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("location does not exists")

with open('ashwa.txt') as file:
    print(file.read())

text ="Hi all.\nThis is ashwanth"
with open('ashwa.txt','w') as file:
    print(file.write(text))

#copy function

import shutil

shutil.copy('ashwa.txt','C:\\Users\\ashwa\\Desktop\\python documents\\ashwanth.txt')

#to move a file
import os

src = "ashwa.txt"
dest = "C:\\Users\\ashwa\\Desktop\\python documents\\mvashwa.txt"

if os.path.exists(dest):
    print("There is already a file")
else:
    os.replace(src,dest)
    print(src +" was moved")