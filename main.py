import tkinter as tk
import math
from time import strftime

# Create the main window
root = tk.Tk()
root.title('Clock')
root.geometry('400x450')

# Create a canvas to draw the analog clock
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Create a label to show the digital clock
digital_label = tk.Label(root, font=('ds-digital', 50), background='white', foreground='black')

# Variable to keep track of the clock mode
analog_mode = True

# Function to draw the analog clock
def draw_analog_clock():
    canvas.delete('all')
    # Draw the clock face
    canvas.create_oval(50, 50, 350, 350, outline='black', width=2)
    
    # Draw the numbers on the clock face
    for i in range(1, 13):
        angle = math.radians((i * 30) - 90)
        x = 200 + 140 * math.cos(angle)
        y = 200 + 140 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=('ds-digital', 20))

    # Get the current time
    current_time = strftime('%I %M %S').split()
    hours = int(current_time[0])
    minutes = int(current_time[1])
    seconds = int(current_time[2])

    # Draw the hour hand
    hour_angle = math.radians((hours * 30) - 90 + (minutes * 0.5))
    hour_x = 200 + 70 * math.cos(hour_angle)
    hour_y = 200 + 70 * math.sin(hour_angle)
    canvas.create_line(200, 200, hour_x, hour_y, width=8, fill='black')

    # Draw the minute hand
    minute_angle = math.radians((minutes * 6) - 90)
    minute_x = 200 + 100 * math.cos(minute_angle)
    minute_y = 200 + 100 * math.sin(minute_angle)
    canvas.create_line(200, 200, minute_x, minute_y, width=6, fill='black')

    # Draw the second hand
    second_angle = math.radians((seconds * 6) - 90)
    second_x = 200 + 120 * math.cos(second_angle)
    second_y = 200 + 120 * math.sin(second_angle)
    canvas.create_line(200, 200, second_x, second_y, width=2, fill='red')

    # Draw the center of the clock
    canvas.create_oval(195, 195, 205, 205, fill='black')

    if analog_mode:
        root.after(1000, draw_analog_clock)

# Function to update the digital clock
def update_digital_clock():
    current_time = strftime('%H:%M:%S %p')
    digital_label.config(text=current_time)
    if not analog_mode:
        root.after(1000, update_digital_clock)

# Function to switch between analog and digital mode
def switch_mode():
    global analog_mode
    analog_mode = not analog_mode
    if analog_mode:
        digital_label.pack_forget()
        canvas.pack()
        root.geometry('400x450')  # Resize for analog clock
        draw_analog_clock()
    else:
        canvas.pack_forget()
        digital_label.pack()
        root.geometry('400x200')  # Resize for digital clock
        update_digital_clock()

# Create a frame for the button to be at the bottom
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

# Create a button to switch between modes
switch_button = tk.Button(button_frame, text='Switch Mode', command=switch_mode)
switch_button.pack()

# Initial call to draw the analog clock
draw_analog_clock()

# Run the application
root.mainloop()
