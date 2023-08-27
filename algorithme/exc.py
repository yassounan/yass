#result=1
#n=int(input("put a number n :\n"))
#for i in range(1,n+1):
 #   result=result*i
    
#print(n,"!= ",result)



#def factorial(n):
 #   if n==1:
  #      return 1
   # return n * factorial(n-1)
    
#n=int(input("put a number n :\n"))
#result=factorial(n)
#print(result)


#def count_down(n):
    #if n==0:
   #     return
  #  print(n)
 #   count_down(n-1)
#n=int(input("put a number n : "))
#count_down(n)


#def sum(n):
   #s=0
  # for i in range(1,n+1):  
  #   s+=i
 #  return s
#n=int(input("put a number n : "))
#result=sum(n)
#print(result)

#def sum(n):
  #  if n==1:
  #      return 1
 #   return n+sum(n-1)
#n=int(input("put a number n :"))
#result=sum(n)
#print(result)

#numbers=[25,16,52,60,80,286,6379]
#sorted_numbers=[]
#def sort_numbers(numbers):

 #   for i in range(max(numbers)+1):
#        if(numbers.count(i)==1):
#            sorted_numbers.append(i)
#sort_numbers(numbers)
#print(sorted_numbers)    




words=["A","C","S","H","B"]
def sort_number(list_of_words):
    n=len(list_of_words)


    for i in range(n):
      for j in range(n-1):
            if list_of_words[j]>list_of_words[j+1]:
                temp=list_of_words[j]
                list_of_words[j]=list_of_words[j+1]
                list_of_words[j+1]=temp
        
    return list_of_words

print("before sorting : \n")
print(words)
print("\n\nafter sorting : \n")
words=sort_number(words)
print(words)



#def count_duplicate(array,item):
  #  count=0
  #  n=len(array)
  #  for number in array:
  #     if number==item:
 #       count+=1
#
#    print(item,"has been found in the array ",count,"times")

#array=[1,8,5,2,1,45,1,63,1,41,1]
#item=int(input ("put an item : "))
#count_duplicate(array,item)




#def checkPalindrome(word):
  #  n=len(word)
   # is_Palindrome=True

   # for i in range(n//2):
     #   if word[i] != word[n-i-1]:
    #        is_Palindrome=False
    #if is_Palindrome:
   #     print(word,"is palindrome")
  #  else:
 #       print(word,"is not palindrome")
#word=str(input("put a word : "))
#checkPalindrome(word)











#def count_duplecate(array,word):
  #  count=0
  #  n=len(array)
 #   for alphabet in array:
 #    if alphabet==word:
 #     count+=1
#    print(word,"has been found ",count,"times")

#array=["A","B","C","D","A","A"]
#word=str(input("put an alphabet :"))
#count_duplecate(array,word)




               