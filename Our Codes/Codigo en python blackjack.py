import pybricks.hubs as hubs
import pybricks.ev3 as ev3
import pybricks.tools as tools

# Initialize the hub and motors
hub = hubs.get_active_hub()
left_motor = ev3.Motor(hub.PORT_A)
right_motor = ev3.Motor(hub.PORT_C)
proximity_sensor = ev3.Sensor(hub.PORT_1)

# Define the square dimensions
square_side_length = 3  # Meters

# Set the initial rotation direction
rotation_direction = 1  # 1 for clockwise, -1 for counterclockwise

# Start the rotation loop
while True:
    # Get the proximity sensor reading
    proximity_value = proximity_sensor.value

    # Check if the sensor detects an obstacle
    if proximity_value > 100:
        # Reverse the rotation direction
        rotation_direction *= -1

    # Rotate the motors in the specified direction
    left_motor.run_at_speed(rotation_direction * 100)
    right_motor.run_at_speed(rotation_direction * 100)

    # Rotate for a specific distance (equivalent to one side of the square)
    distance_to_rotate = square_side_length * 1000  # Convert meters to millimeters
    left_motor.run_until_stalled(distance_to_rotate, speed=rotation_direction * 100)
    right_motor.run_until_stalled(distance_to_rotate, speed=rotation_direction * 100)

    # Stop the motors
    left_motor.stop()
    right_motor.stop()
