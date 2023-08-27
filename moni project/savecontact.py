import json
import os
# create a dict that has
#____name
#____age
#____classe
contact={
    "name" :input("name :"),
    "email":input("email : "),
    "age":input("age : "),
    "classe":input("classe : ")
}
print(contact)






#save it in json_file:
working_directory=os.getcwd()
project_path=os.path.join(working_directory,"project")
contact_json_file=os.path.join(project_path,contact["name"]+"json")
with open(contact_json_file,"w") as contact_file:
        contact_str=json.dumps(contact)
        contact_file.write(contact_str)

