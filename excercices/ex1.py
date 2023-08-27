#with open(r"C:\Users\User\python\excercices\yassin name.text"
   #     ,"r") as file_name:
    #content=file_name.read()
   # print(conte
import json
import os

parrent_path=os.getcwd()
current_path=os.path.join(parrent_path,"exercices")
json_yassin=os.path.join(current_path,"yassin")
pjson_yassin_exists=os.path.exists(json_yassin)
if not json_yassin:
    os.mkdir(json_yassin)
    print("this file is added succesfuly")


#with open(json_yassin,"w"
 #         ,"w") as file_json:
  #  pets=["dog\n","cat\n","tiger\n"]
  #  file_json.writelines(pets)