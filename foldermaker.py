import os


with open('weeks.txt' , 'r' , encoding="utf-8") as fs:
    mylist = fs.read().splitlines()
    muszak = ['Délelőtt' , 'Délután' , 'Éjszaka']
    for i in mylist:
        os.mkdir(i)
        root_path = i
        for j in muszak:
            path = os.path.join(root_path, j)
            os.mkdir(path)
