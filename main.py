from reformFile import reformFile
from createCSV import createCSV
from createGraphFromCSV import createGraphFromCSV
from findEntityName import findEntityName
from removeEmptyWord import lemmatisationInCorpus
from buildTokens import buildTokensInFiles

def main():
    findEntityName()
    lemmatisationInCorpus()
    buildTokensInFiles()
    createCSV()
    createGraphFromCSV()

    

if __name__ == "__main__":
    main()