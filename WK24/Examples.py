with open("E:\\new_file.txt") as file:
    contents = file.read()
    print(contents)


with open("E:\\new_file.txt",mode = 'a') as file:
    file.write("\nNew text.")