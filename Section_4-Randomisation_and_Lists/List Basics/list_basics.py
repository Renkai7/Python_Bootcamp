# List example
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

# Lists
#   choose item in list by position with [0]
print(states_of_america[0])
#   find item at end of list by using [-1]
#   negative counts backwards
print(states_of_america[-1])

#   change list item
states_of_america[1] = "Pencilvania"
print(states_of_america)

#   add item to list using append() function
states_of_america.append("Angelaland")
print(states_of_america)

#  add lists to a list using extend() function
states_of_america.extend(["Disneyland", "Nintendo World", "Fantasy Land"])
print(states_of_america)
