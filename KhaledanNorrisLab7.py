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
    read_file = open(readFile, "r")
    write_file = open(writeFile, "w")
    for line in read_file:
        date, title, budget, gross = line.strip().split(",")
        profit = float(gross) - float(budget)
        print(date, title, profit, sep=",", file = write_file)
    read_file.close()
    write_file.close()

#Gets title of film and its profit(highest)
def title_file(filename):
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
    file_name = checkFile()
    gross = maximumProfit(file_name)
    title=title_file(file_name)
    print("Movie with the highest profit is ",title," with a gross of $",gross,".", sep="")
    print("Enter the name of the file you want to write to.")
    processFile(file_name,checkFile())

#code itself
main()