def are_files_equal(file1, file2):
    file1_content = open("file1", "r")
    file2_content = open("file2", "r")
    if file1_content.read()==file2_content.read():
        return True
    else:
        return False
