#!/bin/python3
import os
import sys
import glob
import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()
device_port = None

KEY_ENTER = b"\x0D"


def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# make function to prompt user the serial port they want to use
def serial_prompt():
    print("Please select the serial port you want to use:")
    ports = serial_ports()

    if len(ports) == 0:
        print("No serial ports found")
        sys.exit(1)

    for i in range(len(ports)):
        print(str(i) + ": " + ports[i])

    port_choice = input("Enter the number of the port you want to use: ")

    # if port_choice is not a number or is not in range of ports, prompt again
    while not port_choice.isdigit() or int(port_choice) not in range(len(ports)):
        clean_terminal()
        print("Invalid port number")
        port_choice = input("Enter the number of the port you want to use: ")

    return ports[int(port_choice)]


def actuate_press(b):
    print("AMPAS:", b)
    print(KEY_ENTER)

    if b == KEY_ENTER:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


#  clean terminal based on OS
def clean_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def main():
    device_port = serial_prompt()
    ser = serial.Serial(device_port, 115200, timeout=1)
    while True:
        b = ser.read()
        actuate_press(b)
        # time.sleep(0.1)


if __name__ == "__main__":
    main()
