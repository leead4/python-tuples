# Create a tuple named zoo that contains your favorite animals.

# Find one of your animals using the .index(value) method on the tuple.

# Determine if an animal is in your tuple by using for value in tuple.

# Create a variable for each of the animals in your tuple with 
# this cool feature of Python.

# # example
# (lizard, fox, mammoth) = zoo
# print(lizard)
# Convert your tuple into a list.

# Use extend() to add three more animals to your zoo.

# Convert the list back into a tuple.

zoo = tuple()
zoo = ("cat", "cat-dog", "catfish", "big-kitty")

my_cat = zoo.index("cat")
print("mycat", my_cat)

# let's find a cat 
for potato in zoo:
	kitty = potato
	if kitty == "cat-dog":
		print("yeah!", kitty)

# example
(cat, cat_dog, catfish, big_kitty) = zoo
print(cat)

# convert to a list
kitty_list = list()

for panda in zoo:
	kitty_list.append(panda)

print(kitty_list)

kitty_list.extend(["panda", "red-panda"])
print(kitty_list)

final_zoo = tuple(kitty_list)

print(final_zoo)






