import os

def list_files(directory):
    os.system(f"ls {directory}")

#Security Vulnerability If the user enters something like ; rm -rf /, the code will execute it!
user_input = input("Enter directory name: ")
list_files(user_input)
