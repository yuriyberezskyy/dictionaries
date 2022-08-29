programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}



#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

#Create and empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit and item in a dictionary
programming_dictionary["Bug"] = "Hello"
print(programming_dictionary)

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# travel_log = {
#   "France": ["Paris", "Little", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

travel_log = {
  "France": {
    "cities_visited":["Paris", "Little", "Dijon"],
    "total_visits": 12
  },
  "Germany":{ 
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
}

travel_log = [{
    "country": "France", 
    "cities_visited":["Paris", "Little", "Dijon"],
    "total_visits": 12
  }, 
  {
    "country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
]