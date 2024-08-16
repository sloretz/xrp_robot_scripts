from XRPLib.defaults import *
import time


def set_initial_positions():
    # Set initial servo positions
    # These are also the positions you need to set them to
    # when building the crossbow.
    print("Ready...")
    servo_one.set_angle(100)
    servo_two.set_angle(100)


def aim_crossbow():
    # Aim the crossbow up.
    # Your exact angles for aiming the crossbow may vary
    # Mine works well between 100 (flat) and 75 (crossbow angled up)
    print("aim...")
    servo_two.set_angle(75)
    time.sleep(1)


def fire_crossbow():
    # Pull the trigger, releasing the rubber band which propels the dart
    print("FIRE!")
    servo_one.set_angle(25)
    time.sleep(0.5)
    servo_one.set_angle(100)
    time.sleep(0.5)


def main():
    
    while True:
        set_initial_positions()
        
        # Push the button labeled "USER" on the board to aim and fire
        board.wait_for_button()
        
        aim_crossbow()
        fire_crossbow()


if __name__ == '__main__':
    main()
