print("Hello World!")

#1. Introduction to Dictionary
#ictionary_name = {key1: value1, key2: value2, key3: value3}

a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
print(a)

#2. Dictionary Operations
#2.1 Accessing Values
print(a["name"])
print(a.get("age"))
print(a["age"])
print(a.get("gender"))

#2.2 Adding and Updating Items
a["city"]="Ranchi"
a["gender"]="male"
print(a)

#2.3 Removing Items from a Dictionary
#Using pop(key)
age=a.pop("age")
print(age)
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
print(a)
a.pop("age")
print(a)
#Using del
del a["course"]
print(a)
#Using popitem()
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
a.popitem()
print(a)
#Using clear()
a.clear()
print(a)

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
