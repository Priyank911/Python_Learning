# file = open("text.txt", "+r")
# data = file.read()
# print(data)
# # print(type(data))

# #To print a single line in python use ---> readline()
# file = open("text.txt", "+r")
# data = file.readline()
# print(data)

# #To print a data in tuple use ---> readlines()
# file = open("text.txt", "+r")
# data = file.readlines()
# print(data)

# #To print a line by line use --> next by next 
# file = open("text.txt", "+r")
# line1 = file.readline()
# print(line1)

# line2 = file.readline()
# print(line2)

# # note if a onces a cursor in file(data) are came at last it point so next in output it show only space or blank...

# line3 = file.readline()
# print(line3)

# file.close()

# To write a data in file.. note if write a data all data already present in the file are delete than after it write

# file = open("text.txt", "+w")
# file.write("Hi Brother..Hi dude...Yo")
# file.close()

# To append data in the last of present data use ---> "a"

# file = open("text.txt", "+a")
# file.write("\nsab badiya ha..")
# file.close()

# If you want to overwrite the txt or data are already present use ---> "r+"
# file = open("text.txt", "+r")
# file.write("Hey ")
# file.close() 
# print(file.read()) # here pointer are at starting point 


# Another way :-----
with open("text.txt", "+r") as f:
    data = f.read()
    print(data)
