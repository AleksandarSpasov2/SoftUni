file_input = input().split('\\')

for element in file_input:
    if "." in element:
        file, extension = element.split(".")

print(f'File name: {file}')
print(f'File extension: {extension}')
