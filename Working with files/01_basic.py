# working with files
import os

#1 Created a csv (test.csv) with personal fields in

#open, print, read, rename
t=open("test.csv","r+")
print("I have opened the file test.csv")
print("Name of the file:", t.name)
print("Closed?:",t.closed)
print("Opening mode:",t.mode)

str1=t.read(17);
print("The string being read is:", str1)
t.close()
print("Closed?:",t.closed)

os.rename("test.csv","new_test.csv")
p=open("new_test.csv","r+")
print("New filename is:", p.name)
p.close()
os.rename("new_test.csv","test.csv")


#make directory, go into it and make a file
full_path="C:/Users/Jen/Documents/GitHub Repositories/Personal Stuff June 2016/Working with files/"
print("This is my directory for this code:", full_path)

print("Does a new_test folder exist?:",os.path.isdir("test_dir"))

if not os.path.isdir("test_dir"):
    os.mkdir("test_dir")
else:
    print("Folder was not created as it already exists - Remove and create a new one.")
    os.rmdir("test_dir")
    os.mkdir("test_dir")
    print("New folder created")

# go into home directory
os.chdir(full_path)
os.chdir("test_dir")
print("Going into new_test folder: ",full_path,"test_dir",sep="")
