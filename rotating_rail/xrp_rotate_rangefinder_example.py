from XRPLib.defaults import *
import time


def sweep_ultrasonic():
    # Give servo time to get to first position
    servo_two.set_angle(10)
    time.sleep(0.5)

    # Print data as a Python list of 2-tuples
    print("data = [")
    # Move servo 5 degrees between range readings
    step = 5
    for angle in range(-90, 91, step):
        # Add 100 to put into Servo range of 0-200 degrees
        servo_two.set_angle(100 + angle)

        # Get ultrasonic sensor readings at 20Hz
        time.sleep(1 / 20)
        distance = rangefinder.distance()
    
        # Filter invalid measurements
        if distance == 0 or distance == rangefinder.MAX_VALUE:
            continue

        print("(" + str(angle) + ", " + str(distance) + "),")
    print("]")


def main():
    print("Ready")
    while True:
        # Push the "USER" button to sweep the sensor
        board.wait_for_button()
        sweep_ultrasonic()


if __name__ == '__main__':
    main()