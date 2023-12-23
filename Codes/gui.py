# In the streaming URL entry, you can use the following format for an IP camera:
# For general format: http://username:password@IP:PORT/video
# Example: http://admin:your_password@192.168.1.100:8080/video
# Make sure to replace 'username', 'password', 'IP', 'PORT', and 'your_password' with the actual credentials and details of your IP camera.
# For more details on accessing IP cameras in Python using OpenCV, refer to the following Stack Overflow post:
# https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv


import subprocess
from tkinter import Tk, Button, OptionMenu, StringVar, Label, Entry


# Initialize detection_process to None
detection_process = None


def run_detection(language_choice, camera_source, streaming_url_entry):  # Add streaming_url_entry as an argument
    global detection_process  # Declare as global to access it outside the function

    # Mapping values to indices
    language_mapping = {"English": 0, "Marathi": 1, "Hindi": 2}
    camera_mapping = {"Default": 0, "USB": 1, "Wireless or IP camera": 2}

    # Get the indices of the selected language and camera source
    language_index = language_mapping[language_choice]
    camera_source_index = camera_mapping[camera_source]

    # Construct the command-line arguments
    command = [
        "python",  # or "python3" depending on your system
        "detect.py",
        "--language-choice", str(language_index),
    ]

    # Add streaming URL to the command if provided
    if camera_source == "Wireless or IP camera":
        streaming_url = streaming_url_entry.get()
        if streaming_url:
            command.extend(["--source", str(streaming_url)])
    else:
        command.extend(["--source", str(camera_source_index)])
    
    # Run the detect.py script
    detection_process = subprocess.Popen(command)


# Create a button to stop detection
def stop_detection_gui():
    global detection_process
    # Terminate the child process gracefully
    if detection_process:
        detection_process.terminate()
        detection_process.wait()


# Function to handle the option change event
def on_camera_change(*args):
    selected_camera = camera_source_var.get()
    if selected_camera == "Wireless or IP camera":  # If WiFi camera is selected, show the streaming URL entry
        # streaming_url_entry.insert(0, "http://10.40.13.230:8080/video")
        streaming_url_entry.config(state='normal')
    else:  # Otherwise, hide the streaming URL entry
        # streaming_url_entry.insert(0, "Only for Wireless or IP camera")
        streaming_url_entry.config(state='disabled')


def on_closing():
    stop_detection_gui()
    root.destroy()

# -------------------------------------------------------------------------------------------------------------------------------------


# Example usage with a fictional GUI library (replace with your actual GUI library)
root = Tk()
root.title("Traffic Sign Detection")
root.geometry("700x350")
root.configure(bg='palegreen')

Label(root, text="Traffic Sign Detection", font="arial 20 bold", bg='palegreen').place(x=215, y=30)

# Create StringVars to store user selections
language_choice_var = StringVar(root)
language_choice_var.set("English")  # Default to English

camera_source_var = StringVar(root)
camera_source_var.set("Default")  # Default to default camera
camera_source_var.trace_add("write", on_camera_change)  # Add trace to detect changes in camera source


# Label for language selection
Label(root, text="Choose Language", font='arial 15 bold', bg='palegreen').place(x=60, y=90)

# Create OptionMenu for language selection
language_menu = OptionMenu(root, language_choice_var, *["English", "Marathi", "Hindi"])
language_menu.config(bg='salmon', font='arial 13 bold', width=20)
language_menu.place(x=320, y=90)

# Label for camera source selection
Label(root, text="Choose Camera Source", font='arial 15 bold', bg='palegreen').place(x=60, y=140)

# Create OptionMenu for camera source selection
camera_menu = OptionMenu(root, camera_source_var, *["Default", "USB", "Wireless or IP camera"])
camera_menu.config(bg='turquoise', font='arial 13 bold', width=20)
camera_menu.place(x=320, y=140)


# Label and Entry for streaming URL
streaming_url_label = Label(root, text="Enter Streaming URL", font='arial 15 bold', bg='palegreen')
streaming_url_label.place(x=60, y=190)

streaming_url_entry = Entry(root, font='arial 13', width=40, borderwidth=2, relief="solid")
streaming_url_entry.place(x=320, y=190)


# Create a button to run detection
run_button = Button(root, text="Run Detection", bg='Green', command=lambda: run_detection(language_choice_var.get(), camera_source_var.get(), streaming_url_entry))
run_button.config(font='arial 15 bold')
run_button.place(x=180, y=250)

# Create a button to stop detection
stop_button = Button(root, text="Stop Detection", bg='Red', command=stop_detection_gui)
stop_button.config(font='arial 15 bold')
stop_button.place(x=350, y=250)


# Set the function to be called when the window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)


try:
    root.mainloop()
except KeyboardInterrupt:
    pass  # Do nothing if KeyboardInterrupt occurs (expected when stopping GUI)
except Exception as e:
    print(e)

# ---------------------------------------------------------------------------------------------------------------------------------


# Ensure that the detection subprocess is terminated before exiting
if detection_process:
    detection_process.terminate()
    detection_process.wait()
