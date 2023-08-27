#with open(r"yassin.text","w")as file_name:
      #  names=["fawzi","moemen","yassin"]
       # file_name.writelines(names)
       # print("the folder has been created")
import os

parent_path= os.getcwd()
list_of_folders=os.listdir(parent_path)
print(list_of_folders)
  

