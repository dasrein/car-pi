MAX_BRIGHTNESS = 255
CONFIG_FILE = "brightness"  # "/sys/class/backlight/10-0045/brightness"
current_value = 0


def read_value():
    try:
        with open(CONFIG_FILE, "r") as file:
            value = file.readline()
            current_value = value
            print(current_value)
    except:
        print("ERROR: Could not read file")


def write_value(value):
    try:
        with open(CONFIG_FILE, "w") as file:
            file.write(str(value))
    except:
        print("ERROR: Could not write to file")


read_value()
write_value(99)
