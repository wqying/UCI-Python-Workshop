# A list is used to store multiple values together
# lists are built into the language, unlike numpy arrays

odds = [1, 3, 5, 7]  # create a list
print("Odds are:", odds)  # the result will be [1, 3, 5, 7], in []s
print("First element:", odds[0])
print("Last element:", odds[3])
print("Last element:", odds[-1])

# We can manipulate the elements in a list, but not in strings
names = ["Pyrite", "Crow", "Garnet"]
print("Names are originally:", names)
names.insert(1, "Aurum")  # we are adding a new element into the list
print("New names:", names)

salsa = ["Peppers", "Onions", "Cilantro", "Tomatoes"]
print("Normal salsa ingredients:", salsa)
my_salsa = salsa
salsa[0] = "hot peppers"  # we're changing the first element in the list
print("Ingredients in my salsa:", my_salsa)

teams = ["SWLD", "Immortals", "QingWei", "EastWind"]
print("Popular teams:", teams)
teams.pop()  # remove the last element from the list
print("Teams that are chill:", teams)

# More functions we can use with lists
games = ["hsr", "genshin", "zzz", "ff14", "pubg"]
print("Games I like:", games)
games.append("arknights")
mid_game = games.pop(2)  # removed zzz from games, and save it into a variable
print("Goated games:", games)
print("Mid games:", mid_game)
games.reverse()  # note that the reversed list cannot be stored into a variable
print("Games reversed:", games)

# Want to repeatedly use the contents of a list and want to make a separate list out of it
gacha_games = list(games)
gacha_games.pop(1)
gacha_games.pop(1)
print(gacha_games)
gacha_games.append("e7")
print("Games that bring me joy:", games)
print("Money suckers:", gacha_games)

# Nested lists
x = [["pepper", "zucchini", "onion"],
     ["cabbage", "lettuce", "garlic"],
     ["apple", "pear", "banana"]]
print(x[0])  # result: ["pepper", "zucchini", "onion"]
print([x[0]])  # result: [["pepper", "zucchini", "onion"]]
print(x[0][0])  # result: pepper

# Showcasing the difference between strings and lists:
long_name = "Batholomew Diggensburke"
first_name = long_name[0:10]
print("First name:", first_name)

last_name = long_name[11:23]  # remember that python counting excludes the last one
print("Last name:", last_name)

people = ["Kaitlen", "Paige", "Maksim", "Lo"]
guys = people[2:4]
print("Male dancers:", guys)

girls = people[0:2]
print("Female dancers:", girls)
