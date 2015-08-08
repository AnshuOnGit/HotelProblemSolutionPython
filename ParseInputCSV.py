__author__ = 'anshukum'

def parseInputCSV():
    with open('input.csv','r') as file:
        return file.readlines()