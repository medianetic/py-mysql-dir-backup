import shutil
import time
import os
import sys
import pathlib
import zipfile

from functions import zipdir                                    

# timestamp stores the time in seconds
timestamp = str(int(time.time()))

## Backup DB
print("Files/MySQL-Copy-Tool\n")
print("1. Backup database")

DB_DATABASE = input("\nDB-Name: ")
DB_USER = input("\nDB-User: ")
DB_PASS = input("\nDB-Password: ")

if not DB_DATABASE:
    sys.exit("Error: No DB-Name defined")

if not DB_USER:
    sys.exit("Error: No DB-User defined")

if not DB_PASS:
    sys.exit("Error: No DB-Passwort defined")

HOST='localhost'
PORT='3306'

os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,DB_DATABASE,DB_DATABASE+"_"+timestamp))
    
print("\n|| Database dumped to "+DB_DATABASE+"_"+timestamp+".sql || ")

print("2. Directory Backup")

currentpath = pathlib.Path().resolve()
currentpythonscript = __file__

print("\nYou are currently working in "+str(currentpath))

target_dir = input("\nWhich directory you want to copy (default (ENTER) for current: ")

if not target_dir:
    target_dir="./"

dirExists = os.path.exists(target_dir)    

## Check if dir exists
if dirExists:
    ## Set filename
    target_filename = input("\nFilename for zip archive (default (ENTER) for "+timestamp+".zip: ")

    if not target_filename:
        target_filename= timestamp+".zip"

    ## ZIP 
    zipf = zipfile.ZipFile(target_filename, 'w', zipfile.ZIP_DEFLATED)
    zipdir(target_dir, zipf)
    zipf.close()

    print("\nZip archive created. Done.")

else:
    sys.exit("Error: Directory does not exists")