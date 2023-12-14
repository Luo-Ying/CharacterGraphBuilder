from reformFile import reformFile
from createCSV import process_corpus
from createGraphFromCSV import createGraphFromCSV

def main():
    userOption = input("Reforme file? (y/n)")
    if userOption == "y": reformFile()
    process_corpus()
    createGraphFromCSV()

    

if __name__ == "__main__":
    main()