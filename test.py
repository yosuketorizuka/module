from myModules import zzModules

importFilePath = r'DiffTool/import/'
importFileName1 = r'Trends_in_deaths1.csv'


if __name__ == "__main__":
    
    readFile = zzModules.readFileClass()
    readFile.setPara(importFilePath, importFileName1)
    dfFile = readFile.readFile()

    getCol = zzModules.getColClass()
    getCol.setPara(dfFile)
    listCol = getCol.getCol()

    pass