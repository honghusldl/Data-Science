import zipfile

# zip
# with zipfile.ZipFile('19-22 Data.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('2019data.xlsx')
#     my_zip.write('2020data.xlsx')
#     my_zip.write('2021data.xlsx')
#     my_zip.write('2022data.xlsx')

# extract
# with zipfile.ZipFile('19-22 Data.zip','r') as my_zip:
#     #print(my_zip.namelist())
#     my_zip.extractall('Data')

# zip
import shutil
# shutil.make_archive('data','zip','Data')

# extract
shutil.unpack_archive('data.zip','data2')
