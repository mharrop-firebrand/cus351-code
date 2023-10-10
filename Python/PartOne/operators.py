#
#! Arithmetic operators
# + Addition
a = 1
b = 6
print(a + b)

c = a + b
print(c)

# - Subtraction
d = 10
e = 4
print(d - e)
c = d - e
print(c)
c = 10
print(c)

# * Multiplication
f = 6
g = 3
print(f * g)

# / Division Returns a float
h = 10
i = 2
# print(h / i)
print(type(h / i))

# ** Power/Exponent
base = 3
exponent = 3
result = base**exponent
print(result)

# % Modulus (remainder after dividing)
j = 10
k = 3
print(j % k)

# / / Divide and Round Down
l = 10
m = 3
print(l // m)

result = (2 + 3) * 4**2 - 5 / 1
print(result)


#! Assignment Operators
# +=
age = 46
print(age)
age += 2
print(age)

# -=
x = 10
x -= 4
print(x)  # x = x - 4

# *=
z = 7
z *= x
print(z)

# /=
x = 14
x /= 7
print(x)

# **=
x = 3
x **= 2  # Equivilant x = x ** 2
print(x)

# / /=
x = 20
x //= 6
print(x)

#! Comparison Operators
# Equal to  ==
x = 5
y = 5
print(x == y)  # True

# Not equals !=
x = 5
y = 3
print(x != y)  # True

# Greater than >
x = 10
y = 5
print(x > y)  # True

# less than <
x = 10
y = 8
print(x < y)  # False

# Greater than or equal to >=
x = 50
y = 7
print(x >= y)  # True

# less than or equal to <=
x = 5
y = 8
print(x <= y)  # True
