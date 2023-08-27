import json
import os
import pprint

working_directory = os.getcwd()
project_path = os.path.join(working_directory, " moni project")

project_path_exists=os.path.exists(project_path)
if not project_path_exists:
    os.mkdir(project_path)

# get only json files
list_of_all_files = os.listdir(project_path)
list_of_json_files = []
for file in list_of_all_files:
    if file.endswith(".json"):
        path = os.path.join(project_path, file)
        list_of_json_files.append(path)

# get all the content from the json files
contacts = []
for json_file in list_of_json_files:
    with open(json_file, 'r') as f:
        content = f.read()
        contact = json.loads(content)
        contacts.append(contact)


search_input=input("what are you searching of ")
result={}


for contact in contacts:
    if search_input in contact["name"]:
        result=contact
print("the result of your search: ",search_input)
if(len(result)>0):
    pprint.pprint(result)
else:
    print("contact not found")

