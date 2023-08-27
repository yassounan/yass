def create_matrix():
    number_of_rows=int(input("the number of rows :"))
    number_of_columns=int(input('number of colums is  '))
    matrix=[]    
    for i in range(number_of_rows):
        row=[]
        for j in range(number_of_columns):
            number=int(input("put a number : "))
            row.append(number)
   
         
        matrix.append(row)

    print(matrix)


create_matrix()
