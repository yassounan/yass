pets=("chat","chien","poule")
print(pets)
print("the first pet is :",pets[0])
tuple_of_pets=("chat","dog","hamster","chat","chat")
print("the position of hamster :",tuple_of_pets.index("hamster"))
print(tuple_of_pets.count("chat"))

pets=sorted(pets,reverse=True)
for position ,pet in enumerate(pets):
    print("el 7ayawen ",pet,"position of ",position)
names=["yassin","ahmed","mouhamed",'hamma','zaineb','gte',"tcvt"]
print (names)
print(sorted(names,reverse=True))
print(names[::-6])
