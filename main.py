from buildTokens import buildTokensInFiles
from createCSV import createCSV
from createGraphFromCSV import createGraphFromCSV
from findEntityName import findEntityName
from removeEmptyWord import lemmatisationInCorpus


def main():
    findEntityName()
    lemmatisationInCorpus()
    buildTokensInFiles()
    createCSV()
    createGraphFromCSV()

    

if __name__ == "__main__":
    main()