from reformFile import reformFile
from createCSV import createCSV
from createGraphFromCSV import createGraphFromCSV
from findEntityName import findEntityName
from removeEmptyWord import lemmatisationInCorpus
from buildTokens import buildTokensInFiles

def main():
    userOption = input("Reforme file? (y/n)")
    if userOption == "y": reformFile()
    # process_corpus()
    # createGraphFromCSV()
    findEntityName()
    lemmatisationInCorpus()
    buildTokensInFiles()
    createCSV()
    createGraphFromCSV()

    

if __name__ == "__main__":
    main()