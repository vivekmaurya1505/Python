#importing reqired modules

from zipfile import ZipFile

#specifying the zip file name
file_name = "abc.zip"

#opening the zip fie read mode

with ZipFile(file_name,"r") as zip:
    #printing all the the contents of the zip file
    zip.printdir()

    #extracting all the files
    print("Extracting all the files now...")
    zip.extractall()
    print("Done!")
