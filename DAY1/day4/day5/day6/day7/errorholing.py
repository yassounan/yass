
try:
    x=float(input("put a number x : \n"))
    y=float(input("put a number y : \n"))
    print(x/y)
except ValueError:
    print("x or y should be a number")
except ZeroDivisionError:
    print("y should not be zero")
else:
    print("there is no error")
finally:
    print("always work")
