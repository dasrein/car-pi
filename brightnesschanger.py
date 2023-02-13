import tkinter as tk
from tkinter import ttk

MAX_BRIGHTNESS = 255
CONFIG_FILE = "/sys/class/backlight/10-0045/brightness"



def runApp():
  # root window
  root = tk.Tk()
  root.geometry ('330x100')
  root.attributes('-fullscreen', True)
  root.resizable (True, True)
  root.title ('Autocomputer')

  #root.columnconfigure (0, weight=1)
 # root.columnconfigure (1, weight=3)


  # slider current value
  current_value = tk.IntVar ()


  def get_current_value ():
    return (current_value.get ()/MAX_BRIGHTNESS*100)


  def slider_changed (event):
    value_percent = "{: .2f} %".format (get_current_value ())
    value_label.configure (text=value_percent)
    try:
      with open(CONFIG_FILE, "w") as file:
        value = current_value.get ()
        file.write (str(value))
    except:
        print ("ERROR: Could not set brightness")
        #probably file does not exist

  # slider
  slider = ttk.Scale (
  root,
  from_=12,
  to=MAX_BRIGHTNESS,
  orient='vertical', # vertical
  command=slider_changed,
  variable=current_value

  )
  slider.pack(expand = 'yes', fill = 'x')

  # current value label
  # current_value_label = ttk.Label (root, text='Current Value:' )
  # current_value_label.pack(expand = 'yes', fill = 'x')


  # value label
  value_label = ttk.Label (root, text=get_current_value ())
  value_label.pack(expand = 'yes', fill = 'y')


  try:
    with open(CONFIG_FILE, "r") as file:
      value = file.readline ()
      slider.set (int (value))
  except:
    print ("Error: Could not read brightness")

  root.mainloop ()

if (__name__ == "__main__"):
  runApp ()
