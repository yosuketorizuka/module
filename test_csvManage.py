# %%

from pydoc import importfile
import pandas as pd
import csv
from myModules import  zzModules
import myModules

importFilePath = r'import/'
importFileName = r'import.csv'
exportFilePath = r'export/'
exportFileName = r'export.csv'

def readFile():
    
    global df_import_in
    
    read_import = zzModules.readFileClass()
    read_import.setPara(importFilePath, importFileName)
    df_import_in = read_import.readFile()

def writeFile():
    
    write_export = zzModules.writeFileClass()
    write_export.setPara(exportFilePath, exportFileName, df_import_in)
    write_export.writeFile()

if __name__ == "__main__":
    
    readFile()

    writeFile()
    
    print("process completed")
# %%
