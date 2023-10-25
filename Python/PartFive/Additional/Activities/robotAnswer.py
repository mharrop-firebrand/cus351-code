"""Part - 1. Setting Up Our Robot

Let's create a robot class. Begin by setting up the instance variables to keep track of important data related to the robot. Here are the steps:

1. Create a new class called 'DriveBot'
2. Set up a basic constructor (no parameters needed)
3. Initialize three instance variables within our constructor which all default to 0:

    -  motor_speed
    - direction
    - sensor_range

Your Task:
Create a python class called 'DriveBot'. Within this class, create instance variables for 'motor_speed, sensor_range, and direction'. All of these should be initialized to 0 by default. After setting up the class, create an object from the class, set the motor_speed to 5, the direction to 90, and the sensor_range to 10. Use print statements to check your work!

Below is an example of how you can setup instance variables manually:
test_bot = DriveBot()
test_bot.motor_speed = 30
test_bot.direction = 90
test_bot.sensor_range = 25
"""


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0


# Create a class object
robo_1 = DriveBot()
# Manually assign values
robo_1.motor_speed = 30
robo_1.direction = 90
robo_1.sensor_range = 25
# Print the values to confirm changes
print(
    "New motor speed is {}, new direction is {}, new sensor range is: {} ".format(
        robo_1.motor_speed, robo_1.direction, robo_1.sensor_range
    )
)
"""
Part - 2. Adding Robot Logic

Let us add some logic to our class. It would be very useful to be able to control our robot, so let us create a control_bot method which changes the speed and direction. Also create a method called adjust_sensor. This method is used to change the range of our robot's sensors which are used to detect obstacles. Here are the steps:

1. Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for a new direction

2. Replace the instance variables for speed and direction with the input parameters

3. Define another function called adjust_sensor which accepts one additional parameter

4. Replace the instance variable sensor_range with the input parameter

Your Task:
In the 'DriveBot' class, add a method called 'control_bot' which accepts parameters: 'new_speed' and 'new_direction'. These should replace the associated instance variables. Create another method called 'adjust_sensor' which accepts a parameter called 'new_sensor_range' which replaces the 'sensor_range' instance variable. Afterwards, use these methods to rotate the robot 180 degrees at 10 miles per hour with a sensor range of 20 feet. Use the provided print statements to check your code!"""


class DriveBot:
    # Constructor
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    # Control Bot Method
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    # Sensor Adjust Method
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


"""

Part - 3. Enhanced Constructor

It can be tedious manually setting the values for each instance variable after you have created an object from the DriveBot class. You can enhance your constructor to automatically assign the values we provide to the instance variables. Instead of taking zero parameters, you are going to make the constructor take three parameters. Here is what you need to do:

1. Modify the constructor to take three parameters (in addition to self): one for motor_speed, one for direction, and one for sensor_range
2. For the first parameter, make the default value 0
3. For the second parameter, make the default value 180
4. For the third parameter, make the default value 10
5. Within the constructor, replace the instance variables with the variables from the input parameters

Your Task:
Upgrade the constructor in the DriveBot class in order to accept three optional parameters. The constructor can accept 'motor_speed' (which defaults to 0 if not provided), 'direction' (which defaults to 180 if not provided, and 'sensor_range' (which defaults to 10 if not provided). These parameters should replace the associated instance variables. Test out the upgraded constructor by initializing a new robot object with a speed of 35, a direction of 75, and a sensor range of 25."""


class DriveBot:
    # Enhanced Constructor
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    # Control Bot Method
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    # Sensor Adjust Method
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


"""
### Part - 4. Controlling Them All

Let us add a new feature which allows the use to control multiple robots at once. The robots should be able to all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all called all_disabled. We can accomplish this using class variables. Here is how we can do it:

1. Create a new class variable within the DriveBot class called all_disabled and set it equal to False
2. Create a new class variable within the DriveBot class called latitude and set it equal to -999999
3. Create a new class variable within the DriveBot class called longitude and set it equal to -999999
4. Outside of the class, test the class variables by setting the longitude of all robots to 50.0, the latitude to -50.0 and all_disabled to True

Your Task:
Create a class variable called all_disabled which is set to False. Next, create two more class variables called latitude and longitude. Set both of those variables to equal -999999. A third robot has been created below the first two robots. Set the latitude of all of the robots to -50.0 at once. Additionally, set the longitude of the robots to 50.0 and set all_disabled to True. You should be able to set those values using three lines of code."""


class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
