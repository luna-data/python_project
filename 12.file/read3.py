infile=open("12.file/phones.txt","r")
for line in infile:
    line=line.strip()
    print(line)
infile.close()
