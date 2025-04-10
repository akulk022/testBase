import subprocess

#This fixes the OS Injection Vulnerability in the previous commit
def list_files(directory):
    subprocess.run(["ls", directory], check=True)

user_input = input("Enter directory name: ")
list_files(user_input)