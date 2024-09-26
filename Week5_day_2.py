#fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)

#fruits[0] = "pineapple" # re-assign values using this
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#print(fruits.index("coconut"))

# print(fruits[0])

#for fruit in fruits:
    #print(fruit)

cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
print(f"these are list of cars {cars}")
print(f"the first car is {cars[0]}")

#changing the value of the list
cars[0] = "toyota"
print(f"the first car is {cars[0]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")

#adding a new value to the list
cars.append("bugatti")
print(cars)
cars.remove("maserati")
print(cars)

#looping through the list
#otherwise called iterating through the list
for car in cars: 
    #print(len(car))
    #print(car)
    carRequest = input("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)