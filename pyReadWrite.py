nameFile = open("input.txt", "r")
nameContents = nameFile.read()
nameFile.close()

print(nameContents)
reversedName = "".join(reversed(nameContents))
print(reversedName)

reverseNameFile = open("output.txt", "w")
reverseNameFile.write(reversedName)
reverseNameFile.close()

#Challenge 17
# Write a Python program that reads a file named "input.txt",
# reverses its contents, and writes the reversed contents to a file named "output.txt".