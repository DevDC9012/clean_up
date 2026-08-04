import os 
import time

#Add your desktop path here
path = r""


def clean_folder():
    if not os.listdir(path):
        print("The folder is empty. Exiting program...")
        return
    else:
        print("Cleaning folder...")
        delete_files()

def delete_files():
     os.chdir(path)
     for file in os.listdir(path):
        if file.endswith((".txt",".bmp",".docx")):
            os.remove(file)
            print(f"{file} removed")
        else:
            print("no files found")

def check_folder():
            print("checking folder...")
            time.sleep(1)
            folder_contents = os.listdir(r"")
            print(folder_contents)

clean_folder()
check_folder()