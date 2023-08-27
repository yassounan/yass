def swap_listes(liste1,liste2):
    print("before swap : \n ")
    print(liste1)
    print(liste2)
    print("\n\nafter swap : \n")
    new_liste=(liste1[0],liste2[0],liste1[1],liste2[1],liste1[2],liste2[2])
    print("liste 1 : ",new_liste)


liste1=[1,3,5]
liste2=[2,4,6]
swap_listes(liste1,liste2)