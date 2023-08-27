fruit={
    "name":"orange",
    "weight":"10kg",
    "score":8,
    "number":17,
    "aspect":"lisse"
}
print(fruit)
print("i need ",fruit["weight"]," of ",fruit["name"])
print("the weight of the fruit is ",fruit["weight"])
print("the score of the fruit is ",fruit["score"])
print("the size of the fruit is : ",len(fruit))
fruit ["name"]="banana"
fruit["weight"]="9 kg"

del fruit["number"]
fruit.pop("score")
fruit.update({"name":"apple"})
print(fruit)
print("all the keys ! ",fruit.keys())
print("all the values ! ",fruit.values())
print(fruit.get("name"))