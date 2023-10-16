#! Part One
# 2) My electricity bills for the last six months have been 23, 32, 45, 59, 31 and 64 GBP
# What is the average monthly electricity bill over the six months period?
# Write an expression to calculate the mean, and store the result in a variable called average_bi_yearly_electric_bill
# The formula to calculate an average is: Add all the values and divide by the total number of values*
average_bi_yearly_electric_bill = (23 + 32 + 45 + 59 + 31 + 64) / 6
print(average_bi_yearly_electric_bill)

# 3) In this question you're going to do some calculations for a tiler.
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide and 7 tiles long. Tiles come in packages of 6.
# How many total tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
print("Total tiles needed are: ", (9 * 7) + (5 * 7))
print(" Tiles left over will be:", (17 * 6) - 98)

# 4) Consider the following variables:
# carrots = 40
# rabbits = 12
# carrots_per_rabbit = carrots / rabbits
carrots = 40
rabbits = 12
print("Original value", rabbits)
carrots_per_rabbit = carrots / rabbits
print(carrots_per_rabbit)

# Now, let's introduce another line
# rabbits = 24
# What will be the output/value of the following statement:
# carrots_per_rabbit
rabbits = 24
print("Modified value", rabbits)
carrots_per_rabbit = carrots / rabbits
print(carrots_per_rabbit)

# 5)Let us revisit the exercise above where we calculated the average electricity bill.
# Please create 6 variables to hold these values.
# For example, Month_1, Month_2, Month_3, Month_4, Month_5, and Month_6.
# Now, make the following changes to the monthly bill values before calculating the average bi-yearly bill:
# - Increase the first month's bill to 3 times
# - Add 10GBP to fifth month's bill
# - Divide the last month's bill by 0.375
# Calculate the average and use the **print** function to display the result.

Month_1 = 23
Month_2 = 32
Month_3 = 45
Month_4 = 59
Month_5 = 31
Month_6 = 64
print(
    "Average monthly bill is:",
    (Month_1 + Month_2 + Month_3 + Month_4 + Month_5 + Month_6) / 6,
)

# 6) Please create the following two variables
# 1. The current volume of a water reservoir (in cubic metres):
# reservoir_volume = 444.5
# 2. The amount of rainfall from a storm (in cubic metres):
# rainfall = 5 </code>
# Perform the following operations:
#     1. Decrease the rainfall variable by 10% to account for runoff
#     2. Add the rainfall variable to the reservoir_volume variable
#     3. Increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
#     4. Decrease reservoir_volume by 5% to account for evaporation
#     5. Subtract 0.25 cubic metres from reservoir_volume to account for water that's piped to arid regions
#     6. Print the new value of the reservoir_volume variable
# First way to answer the question
reservoir_volume = 444.5
rainfall = 5
rainfall *= 0.9
reservoir_volume = reservoir_volume + rainfall
reservoir_volume *= 1.05
reservoir_volume *= 0.95
reservoir_volume -= 0.25
print(reservoir_volume)

# Second way to answer the question
reservoir_volume = 444.5
rainfall = 5

rainfall -= rainfall * 0.1
reservoir_volume += rainfall
reservoir_volume += reservoir_volume * 0.05
reservoir_volume -= reservoir_volume * 0.05
reservoir_volume -= 0.25
print(reservoir_volume)

# 7) Without executing the code, what do you think will be the output of the following operation:
# print(5 / 0)

# ZeroDivisionError Traceback (most recent call last)
# ~\folder\folder\folder\file.py in <module>
# ----> 1 print( 5 / 0 ) ZeroDivisionError: division by zero


# 8)We would like to compare the population densities between 2 geographical regions namely San Francisco and Rio-de-Janeiro.
# Please create the following four variables:
# sf_population, sf_area = 839162, 231.89
# rio_population, rio_area = 6453682, 486.5
# Now calculate the population densities for both by didiving their population with their area and save the result into new variables.
# For example:
# san_francisco_pop_density = sf_population / sf_area
# Do the same for Rio-de-Janeiro
# Your task is to write code that prints 'True' if San-francisco is denser than Rio, and 'False' otherwise. Please use the 'print' function.

sf_population, sf_area = 839162, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population / sf_area
rio_population_density = rio_population / rio_area

print(san_francisco_pop_density)
print(rio_population_density)

print(
    " Is San-Francisco's population denser than rio",
    san_francisco_pop_density > rio_population_density,
)


#! From the Word Doc Activites
# Data Types
age = 25
temperature = 24.5
city = "YourCity"  # Replace with your actual city name
is_sunny = True
x, y = 10, 5

# Swap values of x and y without using a temporary variable
x, y = y, x

# Arithmetic
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)

# String Concatenation
greeting_1 = "Hello " + "YourName"  # Replace with your actual name
greeting_2 = f"Hello {'YourName'}"
print("Greeting 1:", greeting_1)
print("Greeting 2:", greeting_2)

sentence_1 = "I love " + "Python"
sentence_2 = "I love {}".format("Python")
print("Sentence 1:", sentence_1)
print("Sentence 2:", sentence_2)

# Type Casting
num_str = "25"
num_int = int(num_str) + 5

num_str_2 = str(42) + " is the answer"

# Arithmetic and Type Casting
float_result = float(num_int) * y
int_result = int(float_result)

print("Addition of Integer and Float:", num_int + float_result)
print("Multiplication of Integer and Float:", float_result)
print("Result as Integer:", int_result)
