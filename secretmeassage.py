import os


def rename_filename():
    file_list = os.listdir(r"C:\Users\Abhinav\Desktop\Untitled Export")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is"+saved_path)
    os.chdir(r"C:\Users\Abhinav\Desktop\Untitled Export")
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translat(None, "0123456789"))
    os.chdir(saved_path)


rename_filename()
