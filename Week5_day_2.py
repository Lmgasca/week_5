#list = []
#set = {}
#Tuple = ()

#fruits = ["apple", "orange", "banana", "coconut"]
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

#cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
#print(f"these are list of cars {cars}")
#print(f"the first car is {cars[0]}")

#changing the value of the list
#cars[0] = "toyota"
#print(f"the first car is {cars[0]}")
#cars[-1] = "lamborghini"
#print(f"the last car is {cars[-1]}")

#adding a new value to the list
#cars.append("bugatti")
#print(cars)
#cars.remove("maserati")
#print(cars)

#looping through the list
#otherwise called iterating through the list
#for car in cars: 
    #print(len(car))
    #print(car)
    #carRequest = input("add a new car please: ")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    #print(cars.upper())
    #print(cars)
    #if len(cars) > 10:
        #break

#challenge
# create a list of friends
# make sure the initial list is none
#friends = []
# add a new friend to the list, add at least 5 friends
#friends.append("Max")
#friends.append("abel")
#friends.append("jovanny")
#friends.append("jimenez")
#friends.append("angel")
# remove a friend 
#friends.remove("Max")
# insert a friends at a specific index maybe 2
#friends[2] = "diego"
# print the list of friends
#print(friends)
# loop through the list and print the friends name
#for friend in friends:
   # friendRequest = input("add a new friend please: ")
   # friends.append(friendRequest)
   # print(friends)
  #  print(len(friends))
   # print(friends)
# see if a particular friend is in the list (boolean value)
   # print("jimenez" in friends)
# if the list is greater than 10 break the loop
   # if len(friends) > 10:
   #     break

#fruits = {"apple", "orange", "banana", "coconut"}
#print ("pineapple" in fruits)

#print(fruits[0]) This gives an error

#fruits.add("pineapple") ---adds to the set
#fruits.add("grape")
#fruits.add("blueberry")
#fruits.add("blackberry")
#fruits.add("mango")
#fruits.remove("apple") ---removes from the set
#fruits.pop() ---pops off item at the end
#fruits.clear() ---clears the set

#print(fruits)

#print(fruits.index("apple"))
#print(fruits.count("coconut"))


#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)


# Dictionary = a collection of {key:value} pairs
                #ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi", 
            "China": "Beijing", 
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))

#if capitals.get("Russia"):
#    print("That capital exists")
#else: 
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"}) ---adds to set
#capitals.update({"USA": "Detroit"}) ---changes the currrent set
#capitals.pop("China") ---pops out 
#capitals.popitem() ---pops out last 
#capitals.clear() ---clear

#print(capitals)

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
