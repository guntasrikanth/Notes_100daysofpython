with open('file1.txt') as data:
    file1_data = data.readlines()
file1_list = [int(num) for num in file1_data]
print(file1_list)

with open('file2.txt') as data:
    file2_data = data.readlines()
file2_list = [int(num) for num in file2_data]
print(file2_list)

result = [num for num in file2_list if num in file1_list]
print(result)