#with open(r"C:\Users\User\python\DAY1\day4\day5\day6\day7\names.txt"
       #   ,"r")as name_file:
        #first_line=name_file.readline()
        #print(first_line)




#with open(r"contacts.txt",
 #         "a")as name_file:
  #      name_file.write("mouhamed")

import json
import os


parent_path = os.getcwd()
current_path = os.path.join(parent_path, "new")

current_path_exists = os.path.exists(current_path)
if not current_path_exists:
    os.mkdir(current_path)

moemen_path = os.path.join(current_path, "moemen.json")


data = {
    "name": "ahmed",
    "lastname": "sry heni",
    "age": 16
}

with open(moemen_path, "w") as json_file:
    json_content = json.dumps(data)
    json_file.write(json_content)



    























import json



with open (moemen_path ,"r") as json_file:
    content=json_file.read()
    data=json.loads(content)
    print(content)

    































































































































































#import os



#parent_path=os.getcwd()
#current_path=os.path.join(parent_path,"new")
#ahmed_path=os.path.join(current_path,"ahmed.json")
#print("the path of parent_folder : ",parent_path)
#print("the path of current_folder : ",current_path)
#print("the path of ahmed file :  ",ahmed_path)

#import json


#data={
 #   "name":"ahmed",
  #  "lastname":"sry heni",
   # "age":16
#}

#with open(ahmed_path
 #         ,"w")as json_file:
  #  json_content=json.dumps(data)
   # json_file.write(json_content)
    






