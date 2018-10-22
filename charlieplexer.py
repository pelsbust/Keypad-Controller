import RPi.GPIO as GPIO
import time

pins = [18, 23, 24]

pin_led_states = [
  [1, 0, -1], # A
  [0, 1, -1], # B
  [-1, 1, 0], # C
  [-1, 0, 1], # D
  [1, -1, 0], # E
  [0, -1, 1]  # F
]

GPIO.setmode(GPIO.BCM)


def set_pin(pin_index, pin_state):
    """
    Help function, used to set the state of a pin.

    :param pin_index: The pin which will be set
    :param pin_state: The state the pin will be set to
    :return:
    """
    if pin_state == -1:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)


def light_led(led_number):
    """
    Lights a given led input

    :param led_number:
    :return:
    """
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)


def power_up():
    """

    :return:
    """
    light_led(0)
    time.sleep(0.5)
    light_led(1)
    time.sleep(0.5)
    light_led(2)
    time.sleep(0.5)
    light_led(3)
    time.sleep(0.5)


def power_down():
    """

    :return:
    """
    light_led(3)
    time.sleep(0.5)
    light_led(2)
    time.sleep(0.5)
    light_led(1)
    time.sleep(0.5)
    light_led(0)
    time.sleep(0.5)


def wrong_password():
    """

    :return:
    """


def login_successful():
    """

    :return:
    """


def light_specific_led():
    while True:
        inp = int(input("Pin (0 to 5):"))
        light_led(inp)


set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)

while True:
    x = int(input("Pin (0 to 5):"))
    light_led(x)
