#
#! Strings (str)
# print()
fname = "Maddy"
print(fname)
lname = "Harrop"
print(lname)

# +
fname = "Maddy"
lname = "Harrop"
print(fname + " " + lname)

# ,
name = "Maddy Harrop"
age = 46
print("My name is", name, "and I am", age)


# F String
favourite = "favourite"
fruit = "Apple"
amount = 5
print(f"Emily's {favourite} fruit is {fruit} and they have {amount} {fruit}'s ")

# %
pet_name = "Willow"
willow_age = 7
print("The cat is called %s and they are %d months old." % (pet_name, willow_age))


# .fomat()
pet_name = "Willow"
willow_age = 7
print("The cat is called {} and they are {} months old.".format(pet_name, willow_age))


#! Assignment operators on strings
# Concatenation Assignment (+=)
greeting = "Hello "
name = "Maddy"
greeting += name
print(greeting)

# Repetition Assignment (*=)
word = "python"
word *= 3
print(word)
