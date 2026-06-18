#                             # домашнє завдання


  # виводим кожен елемент з масиву
array_example = [4, 4, 8, 3, 3, 3, 2, 4, 4]
for element in array_example:
     print(element)



    # виводим перші 3 елементи
array_example = [4, 4, 8, 3, 3, 3, 2, 4, 4]
for index in range(3):
     print(array_example[index])


#    # вивести суму всіх елементів
array_example = [4, 4, 8, 3, 3, 3, 2, 4, 4]
print(sum(array_example))



#     # вивести суму всі окрім =4
array_example = [4, 4, 8, 3, 3, 3, 2, 4, 4]

total = 0

for element in array_example:
    if element != 4:
        total += element


print(total)
import json

# виводим данні з файлу test_folders.json
with open("test_folders.json", "r") as test_folders:
    data = json.load(test_folders)
    print(data["name"])
    print(data["id"])



















                                 # examples:

# number_value = 5
# b = ("jsfdns")
# c = {"name":"test"}
# string_value = "Hello"
# string_value_2 = "World"
#
#
# print(b)
# print(c)
# print(string_value + str(number_value))
# print(f"Hello {string_value_2}!")
# import json

# масиви
# array_example = ["appele","banana","cherry","lastelement"]


# перший елемент
# print(array_example[0])


# всі елементи
# print(len(array_example))


# останній елемент
# print(array_example[len(array_example) - 1])
# print(array_example[-1])


# виводим всі елементи
# for element in array_example:
#     print(element)
#
#
# for index in range(20):
#         print(index)


# виводим перші 3 елементи
# for index in range(3):
#     print(array_example[index])


# # виводим данні з файлу test_folders.json
# with open("test_folders.json", "r") as test_folders:
#     data = json.load(test_folders)
#     print(data[name])
# !!!!!!!


# виводим парні числа
# array_example = [2,3,7,23,34,55,62,8]
#
# for element in array_example:
#     if (element % 2 == 0):
#         print(element)




