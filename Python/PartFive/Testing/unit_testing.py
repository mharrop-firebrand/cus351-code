"""
A unit-test usually comprises the following three sections:
Preparation: set-up the scene. Prepare all data, objects, and services you need in the places you need them so they are ready to be used
Execution: execute the bit of logic that you are checking against. You perform an action using the data and the interfaces you have set-up in the preparation phase
Verification: verify results and ensure they are according to your expectations
"""

""" 
Basic unit testing concepts include:
	• Test cases: Scenario or condition that we want to check
	• Fixtures: Prepartion for the test. 
		Set-up fixture: Ensure test enviroment is it a good state
		Tear-down fixture: Cleans up our enviroment
	• Assertions: checks for pass or fail
	• Test suite:
		fixture: 
			Set-up fixture: Ensure test enviroment is it a good state
			Tear-down fixture: Cleans up our enviroment
	• Test Runner: unittest
"""

"""
assertEquals(num, num)
assertNotEquals(num, num)
assertTrue(j)
assertFalse(l)
assertIs(num, num)
"""
import unittest


def add(x, y):
    return x + y


# Our assumption is any value we pass in to x and y will be added to create a sum
class TestAddFunction(unittest.TestCase):
    # Create our own test methods
    # Assertions (what happend) is equal to (what we expected)
    def test_add_positive_numbers(self):
        result = add(5, 3)
        self.assertEquals(result, 8)

    def test_add_negative_numbers(self):
        result = add(-9, -11)
        self.assertEqual(result, -20)


# if current file == file being run
if __name__ == "__main__":
    unittest.main()
