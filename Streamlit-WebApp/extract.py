import zipfile

with zipfile.ZipFile('19-22 Data.zip','r') as my_zip:
    #print(my_zip.namelist())
    my_zip.extractall('Data')