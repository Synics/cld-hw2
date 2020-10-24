import os
import socket


def listTextFiles():
    a = open(outputFileDir + outputFile, "a")
    a.write("Text Files:\n")
    for file in os.listdir(fileDir):
        if file.endswith(".txt"):
            a.write(file + "\n")
    a.close()


def listOtherInformation():
    a = open(outputFileDir + outputFile, "a")
    a.write("Total Words:\n")
    totalWordCount = 0
    maxFileName = ""
    maxWordCount = -1

    for file in os.listdir(fileDir):
        if file.endswith(".txt"):
            txtFile = open(fileDir + file, "r")
            wordCount = len(txtFile.read().split())

            if wordCount > maxWordCount:
                maxWordCount = wordCount
                maxFileName = file

            totalWordCount += wordCount
            a.write(file + ": " + str(wordCount) + "\n")
            txtFile.close()

    a.write("Grand Total Number of Words: " + str(totalWordCount) + "\n")
    a.write("File With the Most Words: " + maxFileName + "\n")
    a.write("Machine IP: " + socket.gethostbyname(socket.gethostname()) + "\n")
    a.close()


fileDir = "/home/data/"
outputFileDir = "/home/output/"
outputFile = "result.txt"

listTextFiles()
listOtherInformation()
output = open(outputFileDir + outputFile, "r")
for line in output.readlines():
    print(line)

















