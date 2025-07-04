import os

#cwd = current working directory
print(os.getcwd())

new_directory = 'abce'
os.mkdir(new_directory)

os.chdir(new_directory)

os.chdir("..")

os.rmdir(new_directory)