def swap_tuples(tuple1 , tuple2):
    print("Before swap : \n")
    print("tuple 1 ",tuple1)
    print("tuple 2 ",tuple2)
    print("\n\nAfter swap : \n ")
    new_tuple1=(tuple2[0],tuple1[1],tuple2[2])
    new_tuple2=(tuple1[0],tuple2[1],tuple1[2])
    print("tuple 1 ",new_tuple1)
    print("tuple 2 ",new_tuple2)
tuple1=[1,2,3]
tuple2=[4,5,6]
swap_tuples(tuple1 , tuple2)