import json


pet={
    "name":"yoyo",
    "type":"cat",
     "age":4
}

#C:\Users\User\python\DAY1\day8\json\dump.json

with open(r"C:\Users\User\python\DAY1\day8\json\pet.json"
          ,"w")as pet_file:
    pet_json=json.dumps(pet)
    pet_file.write(pet_json)
    print("file has been created !")

 






































































































































#with open(r"C:\Users\User\python\DAY1\day8\json\dump.json"
   #       ,"w")as dump_file:
  #  dump_pet=json.dumps(pet)
  #  dump_file.write(dump_pet+"\n")    