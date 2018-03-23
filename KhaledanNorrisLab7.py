#Programmers: Jake Norris and Alex Khaledan
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
            open(filename, "r")
            return filename
        except:
            print("Sorry, that wasnt a valid file > ")

#Calculates the max profit and returns
def maximumProfit(filename):
    with open(filename, "r") as file:
        maxProfit = 0
        for line in file:
            date, title, budget, gross = line.strip().split(",")
            profit = float(gross)-float(budget)
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

#writes to user inputted file after reading
def processFile(readFile, writeFile):
    readFile = open(readFile, "r")
    writeFile = open(writeFile, "w")
    for line in readFile:
        date, title, budget, gross = line.strip().split(",")
        profit = float(gross) - float(budget)
        print(date, title, profit, sep=",", file = writeFile)
    readFile.close()
    writeFile.close()

#Gets title of film and its profit(highest)
def maximumTitle(filename):
    with open(filename, "r") as file:
        maxProfit = 0
        for line in file:
            date, title, budget, gross = line.strip().split(",")
            profit = float(gross)-float(budget)
            if profit > maxProfit:
                maxProfit = profit
                maxTitle = title
    return maxTitle

def main():
    print("This program will calculate the movie with the maximum profit.")
    print("Which file would you like to calculate the maximum profit from? ")
    filename = checkFile()
    profit = maximumProfit(filename)
    title = maximumTitle(filename)
    print("Movie with the highest profit is ",title," with a profit of $", profit ,".", sep="")
    print("Enter the name of the file you want to write to: ", end="")
    processFile(filename,input(""))

#code itself
main()