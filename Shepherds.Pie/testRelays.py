import gpiozero
import time

# Constants
SLEEP_TIME = 1
TRIGGER_DURATION = 0.5

# Assign the pins
RELAY_1_PIN = 18
RELAY_2_PIN = 23
RELAY_3_PIN = 24
RELAY_4_PIN = 25

# Create the relay 'switches'
sound1 = gpiozero.OutputDevice(RELAY_1_PIN, active_high=False, initial_value=False)
sound2 = gpiozero.OutputDevice(RELAY_2_PIN, active_high=False, initial_value=False)
sound3 = gpiozero.OutputDevice(RELAY_3_PIN, active_high=False, initial_value=False)
sound4 = gpiozero.OutputDevice(RELAY_4_PIN, active_high=False, initial_value=False)

def reset_relays():
    print("Turning off relay 1")
    sound1.off()
    print("Turning off relay 2")
    sound2.off()
    print("Turning off relay 3")
    sound3.off()
    print("Turning off relay 4")
    sound4.off()


def trigger_sound(soundRelay):
    soundRelay.on()
    time.sleep(TRIGGER_DURATION)
    soundRelay.off()

def test_loop():
    reset_relays()
    while 1:
        print("Triggering relay 1")
        trigger_sound(sound1)
        time.sleep(SLEEP_TIME)

        print("Triggering relay 2")
        trigger_sound(sound2)
        time.sleep(SLEEP_TIME)

        print("Triggering relay 3")
        trigger_sound(sound3)
        time.sleep(SLEEP_TIME)

        print("Triggering relay 4")
        trigger_sound(sound4)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    try:
        test_loop()
    except KeyboardInterrupt:
        reset_relays()
