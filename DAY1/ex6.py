def swap_list(list1):
    n=int (input ("put a number n : \n "))
    print("Before swap : \n")
    print("list 1 : ",list1)
    print("\n\nAfter swap : \n")
    new_list=[list1[2],list1[0],list1[1],n]
    print("list 1 : ",new_list)
list1=[1,2,4]
swap_list(list1)

