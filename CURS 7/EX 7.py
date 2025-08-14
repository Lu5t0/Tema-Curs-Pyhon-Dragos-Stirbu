files = ['mare_2023.jpeg', 'test.txt', 'liste.py', 'cv.pdf']
paths = {
    'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
    'C://Downloads//Text': ['txt'],
    'C://Downloads//Python_files': ['py'],
    'C://Downloads//PDF': ['pdf'],
}
locatie_files = {}
for path, fisiere in paths.items() :
    if fisiere == paths['C://Downloads//Images']:
        locatie_files[files[0]] = 'C://Downloads//Images'
    elif fisiere == paths['C://Downloads//Text']:
        locatie_files[files[1]] = 'C://Downloads//Text'
    elif fisiere == paths['C://Downloads//Python_files']:
        locatie_files[files[2]] = 'C://Downloads//Python_files'
    elif fisiere == paths['C://Downloads//PDF']:
        locatie_files[files[3]] = 'C://Downloads//PDF'

print(locatie_files)




