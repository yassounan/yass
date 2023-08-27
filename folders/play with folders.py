import os


parent_path=os.getcwd()
current_path=os.path.join(parent_path,"folders")
yassin_path=os.path.join(current_path,"yassin")
print("the path of parent_folder : ",parent_path)
print("the path of current_folder : ",current_path)


try:
   os.mkdir(yassin_path)
except FileExistsError:
   print("we already have this folder")