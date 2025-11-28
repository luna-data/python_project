import os

def calcDirsize(name):
    totalSize = 0

    if os.path.isfile(name):
        totalSize += os.path.getsize(name)
    else:
        fileList = os.distdir(name)
        for subDir in fileList :
            totalSize += calcDirsize(os.path.join(name, subDir))
    
    return totalSize

name = input("디렉토리 이름을 입력하시오 :")
print(calcDirsize(name))