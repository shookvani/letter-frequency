#LetterFrequency.py
#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message,inputFilename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26

    for letter in message:
        spot = alpha.find(letter)
        if spot >= 0:
            freq[spot] += 1

    freqFile = open(inputFilename+'.csv', 'w')

    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        freqFile.write(line)

    freqFile.close()

def main(inputFilename):
    #inputFilename=input("Enter filename:")
    fileObj = open(inputFilename,'r')
    content = fileObj.read()
    fileObj.close()
    countLetters(content,inputFilename)

#main()
