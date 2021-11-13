import zipfile

with zipfile.ZipFile('19-22 Data.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('2019data.xlsx')
    my_zip.write('2020data.xlsx')
    my_zip.write('2021data.xlsx')
    my_zip.write('2022data.xlsx')