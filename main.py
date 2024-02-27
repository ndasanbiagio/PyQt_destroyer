from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames # Not is good practice
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select Files')
    message.setText('\n'.join(filenames)) 
    

def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successful!')
    

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File') # Placeholder
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()


#Let's break down the code step by step:

# Imports:

# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, 
# QPushButton, QFileDialog: These are imports from the PyQt6 library, used for creating GUI applications.
# from PyQt6.QtCore import Qt: This import is for accessing Qt constants.
# from pathlib import Path: This import is for handling file paths in a platform-independent manner.
# Global Variables:

# filenames: This variable is used to store the paths of the files selected for destruction. 
# Note: Using global variables is generally discouraged due to potential issues with readability and maintainability.
# Functions:

# open_files(): This function is called when the "Open Files" button is clicked. It opens 
# a file dialog (QFileDialog) to allow the user to select one or more files. The selected 
# file paths are stored in the filenames variable, and a message is displayed showing the selected file paths.
# destroy_files(): This function is triggered when the "Destroy Files" button is clicked.
# It iterates over each selected file path stored in filenames, wipes the contents of each 
# file, and then deletes them permanently. Finally, it updates the message label to indicate that the destruction process was successful.
# Main Application Setup:

# app = QApplication([]): Initializes the PyQt application.
# window = QWidget(): Creates the main application window.
# window.setWindowTitle('File Destroyer'): Sets the window title.
# layout = QVBoxLayout(): Creates a vertical box layout to arrange widgets vertically within the window.
# Widgets:

# description: A label displaying instructions to the user.
# open_btn: A button labeled "Open Files" that triggers the open_files() function.
# destroy_btn: A button labeled "Destroy Files" that triggers the destroy_files() function.
# message: A label used to display status messages to the user.
# Layout Setup:

# Widgets are added to the layout using addWidget() method.
# Buttons are connected to their respective functions using clicked.connect() method.
# Layout is applied to the window using setLayout() method.
# Application Execution:

# window.show(): Displays the main window.
# app.exec(): Starts the PyQt application event loop, allowing the application to respond to user interactions.
# Overall, the code creates a simple GUI application using PyQt6, allowing users to select and destroy files.