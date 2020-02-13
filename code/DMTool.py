import tkinter as tk
import time
import sys

# Define a test screen
class TestScreen(tk.Frame):
    def __init__(self, parent):
        super(TestScreen, self).__init__(parent)

        # Add message to window
        self.label = tk.Label(self, text="Hello World")
        self.label.pack(padx=10, pady=10)

# Define quit function
def __close(event):
	"""Quit program
	Consumes user input and closes the program"""
	sys.exit() 

# Main for testing, This will allow the user to specify a test csv file.
def __main():
	# Define the window
	root= tk.Tk()
	main = TestScreen(root)
	main.pack(fill="both", expand=True)

	# Program the window to close the window
	#	- Close the window on Escape or Return
	root.bind('<Escape>', __close)
	root.bind('<Return>', __close)

	# Call the main loop
	root.mainloop()


if __name__ == '__main__':
    __main()
