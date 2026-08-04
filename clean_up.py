import os 
import time


path = r"C:\Users\Dev\Desktop"


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
            folder_contents = os.listdir(r"C:\Users\Dev\Desktop")
            print(folder_contents)

clean_folder()
check_folder()