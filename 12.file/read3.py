infile=open("phones.txt","r")
for line in infile:
    line=line.strip()
    print(line)
infile.close()
