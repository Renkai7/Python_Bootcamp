with open("file1.txt") as file_1:
    file_1_list = file_1.read().splitlines()

with open("file2.txt") as file_2:
    file_2_list = file_2.read().splitlines()

result = [num for num in file_1_list if num in file_2_list]

print(file_1_list)
print(file_2_list)

# Write your code above 👆

print(result)