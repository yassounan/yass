#def sum (n):
   
   #s = 0

   #for i in range(1,n+1):
  #   s+=i
 #    return s
#n=int (input("put a number n : "))
#somme=sum(n)
#print(somme)


#numbers=[14,52,12,75]
#sorted_numbers=[]
#def sort_numbers(numbers):

   # for i in range(max (numbers)+1):
  #    if(numbers.count(i)==1):
 #       sorted_numbers.append(i)
#sort_numbers(numbers)
#print(sorted_numbers)
   
   
#numbers=[16,28,9,36]

#def sort_numbers(list_of_numbers):
    #n=len(list_of_numbers)


    #for i in range (n):
     #for j in range(n-1):
     #      if list_of_numbers[j]<list_of_numbers[j+1]:
    #           temp=list_of_numbers[j]
   #            list_of_numbers[j]=list_of_numbers[j+1]
  #             list_of_numbers[j+1]=temp
        
 #   return list_of_numbers
     
#print("before sorting : \n")
#print(numbers)
#print("\n\nAfter sorting : \n")
#numbers=sort_numbers(numbers)











def search(array,item):
    position=None
    for i in range(len(array)):
        print("checking ",array[i],"and ",item)
        if array[i]==item:
            position=i
            break
    
    if position==None:
        print("not found")
    else:
        print(item,"found at position ",position)
  
array=[16,22,71,25]
item=int(input("put a number n : "))
search(array,item) 

    