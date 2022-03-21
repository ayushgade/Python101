reading_files = open("names.txt", "r+")
# print(reading_files.readline())
# print(reading_files.readline())
# print(reading_files.readline())
for name in reading_files.readlines():
    print(name)
reading_files.close()