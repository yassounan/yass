import json

pets={
    "name":"max",
    "type":"chien",
    "age":2
}


with open(r"C:\Users\User\python\DAY1\day8\json\pet.json"
          ,'w')as file_pets:
    json_pets=json.dumps(pets)
    file_pets.write(json_pets)
    
    print(file_pets)
    print("folder has been created")

import json

homme={
  "name":"yassin",
  "age":16,
  "city":"makthare"
}
try:        
         with open(r"C:\Users\User\python\DAY1\day8\json\pet.json"
           ,'w')as file_homme:
            json_homme=json .dumps(homme)
            file_homme .write(json_homme)
            print(json_homme)
except SyntaxError:
     print("make sure about the  :")











































































































#try :
   # with open(
   # r"C:\Users\User\python\DAY1\day8\yassin","r") as name_file:
     #   content=name_file.read()
  #  print(content)
#except(FileNotFoundError,FileExistsError):
   # print("File doesn't exist!")
#except SyntaxError:
 #   print("make sure to use 'r' for windows ")     