infile=open("12.file/phones.txt","r")
line=infile.readline()
while line !="":
    print(line)
    line=infile.readline()
infile.close()