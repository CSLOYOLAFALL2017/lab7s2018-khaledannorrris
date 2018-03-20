#Programmers:Jake Norris and Alex Khaledan
# Course:  CS151.01, Professor Franceschi
# Date: March 20, 2018
# Lab Assignment:  7
# Problem Statement:  Determine highest profit from list of films and their data
# Data In: filename.
# Data Out: Highest profit and its title.
# Other files needed: user inputted.
# Credits: None



#Gets valid filename from user
def checkFile():
    validInput = False
    while not validInput:
        try:
            filename = input("Enter a file > ")
            file = open(filename, "r")
            return filename
        except:
            print("Sorry, that wasnt a valid file > ")
#calculates the max profit and returns
def maximumGross(filename):
    with open(filename, "r") as file:
        maxGross = 0
        for line in file:
            date, title, budget, gross = line.strip().split(",")
            profit = float(gross)-float(budget)
            if profit > maxGross:
                maxGross = profit
    return maxGross
#writes to user inputted file after reading
def processFile(readFile, writeFile):
    read_file = open(readFile, "r")
    write_file = open(writeFile, "w")
    for line in read_file:
        date, title, budget, gross = line.strip().split(",")
        print("Hello", date, title, gross, sep=",", file = write_file)
    read_file.close()
    write_file.close()
#Gets title of film and its profit(highest)
def title_file(filename):
    with open(filename, "r") as file:
        maxGross = 0
        for line in file:
            date, title, budget, gross = line.strip().split(",")
            profit = float(gross)-float(budget)
            if profit > maxGross:
                maxGross = profit
                maxTitle=title
    return maxTitle

def main():
    file_name=checkFile()
    gross=maximumGross(file_name)
    title=title_file(file_name)
    print("movie with the highest gross is",title,"with a gross of",gross,".")
    processFile(file_name,checkFile())

#code itself
main()