from pathlib import Path
import os

def readfileandfolder():
    path = Path("")
    dirs = list(path.rglob("*"))
    for i,v in enumerate(dirs):
        print(f"{i} - {v}")
print("press 1 for creating a folder")
print("press 2 for reading a folder")
print("press 3 for updating a folder")
print("press 4 for deleting a folder")
print("press 0 for exiting the folder")

check = input("please tell what you want to do")



while(True):
    if check == "1":
        dirpath = input("please tell the name of your folder")
        path = Path(dirpath)
        path.mkdir()
        print("your folder is created")
        break

    elif check == "2":
        readfileandfolder()

    elif check == "3":
        readfileandfolder()
        hello = input("which folder yoou want to update")
        path = Path(hello)
        path.rename(input("type your new folder name"))
        print("successfully done")

    elif check == "4":
        readfileandfolder()
        hello = input("which folder you want to delete")
        path = Path(hello)
        path.rmdir()
        print("successfully done")





