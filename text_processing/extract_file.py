file_name = input().split("\\")[-1]
name = file_name.split('.')[0]
extension = file_name.split('.')[1]

print(f"File name: {name}")
print(f"File extension: {extension}")
