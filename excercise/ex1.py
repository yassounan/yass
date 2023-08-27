#counter=0
#while (counter<10




import json


person_dict={}
with open(r"C:\Users\User\python\DAY1\day8\json\pet.json"
          ,'r') as json_file:
    content=json_file.read()
    person_dict=json.loads(content)
    

person_dict["email"]="yassin@gmail.com"
    
with open(r"C:\Users\User\python\DAY1\day8\json\pet.json"
          ,"w") as json_file:
    person_str=json.dumps(person_dict)
    json_file.write(person_str)

    