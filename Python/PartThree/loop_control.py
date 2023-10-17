#
#! Loop Control
# Break
# Continue
# Pass

#! Break
"""The while loop is iterating from i = 1 to i = 10
When i becomes equal to 5, the break statement is encountered
The loop terminates immediately, without printing 5, 6, ..., 10"""
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

print("Hi")
# or
for i in range(1, 11):
    print(i)
    if i == 5:
        break

#! Continue
"""The for loop is iterating from i = 1 to i = 5
When i is equal to 3, the continue statement is encountered it skips printing 3 and moves to the next iteration, printing the remaining values."""
# for i in range(1, 101):
#     if i >= 5 and i <= 95:
#         print("It got to 3 and skipped")
#         continue
#     print(i)

#! Pass
"""The loop will iterate three times, and inside the loop, we have a placeholder for a condition that will be implemented later.
The pass statement ensures that the loop doesn't produce any errors even if the condition is not implemented yet."""
for i in range(3):
    pass
    # Something will be implemented later after more thought
