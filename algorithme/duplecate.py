#def count_duplicate(array,item):
  #  count=0
   # n=len(array)
    #for number in array:
     #   if number==item:
      #      count+=1
    
   # print(item,"has been found in the array ",count,' times.')

#array=[34,5,86,5,94,5,87,5]
#item=int(input("put a number n : "))

#count_duplicate(array,item)


names=["A","S","F","M","Y"]

def sort_names(list_of_names):
  n=len(list_of_names)

  for i in range(n):
   for j in range(n-1):
         if  list_of_names[j]>list_of_names[j+1]:
               temp=list_of_names[j]
               list_of_names[j]==list_of_names[j+1]
               list_of_names[j+1]=temp

  return list_of_names
   
print("before sorting : \n")
print(names)
print("\n\nAfter sorting : \n")
names=sort_names(names)
print (names)