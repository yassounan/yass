names=[]
for i in range(4):
    name=input("put a name : \n")
    names.append(name+"\n")


name_file=open(r"C:\Users\User\python\DAY1\utfukhb","a")
name_file.writelines(names)
name_file.close()
