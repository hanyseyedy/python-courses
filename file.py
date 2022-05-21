# testTextFile = open('./test.txt')

# print(testTextFile.read())
# testTextFile.seek(0) # move corser to start of file
# print(testTextFile.read())
# print(testTextFile.readline())

# testTextFile.close()

# with open('./test.txt') as File:
#     print(File.read())
#     File.seek(0)
#     print(File.read())

with open('./test.txt', mode='w') as File:
    File.write('hello\nNew text writed\n')

with open('./test.txt', mode='a') as File:
    File.write('hello\nSecond text writed')