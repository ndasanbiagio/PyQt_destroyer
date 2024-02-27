# PyQt_destroyer
PyQt File Destroyer

File Destroyer
This simple Python application allows you to permanently delete files by selecting them through a graphical interface. 
Once selected, the chosen files will be destroyed, and their contents will be irrecoverably wiped.

Prerequisites
Python 3.x
PyQt6 library
How to Use
Open Files: Click on the "Open Files" button to select the files you want to destroy using the file dialog.
Destroy Files: After selecting the desired files, click on the "Destroy Files" button to permanently delete them.
Confirmation: Upon successful destruction, a message will be displayed confirming the action.
Important Notes
Permanence: This action is irreversible. Once files are destroyed, their contents cannot be recovered.
Use with Caution: Exercise caution while using this tool, ensuring that you only destroy files you intend to permanently erase.
Global Variables: Note that the use of global variables (filenames) is not considered best practice and may impact code readability and maintainability.
Code Overview
The application is built using PyQt6 library for the graphical interface. Here's a brief overview of the code:

open_files(): Opens a file dialog to select files for destruction and displays their paths.
destroy_files(): Permanently deletes the selected files by wiping their contents.
The UI consists of a window with two buttons (Open Files and Destroy Files) and a message label.
Running the Application
To run the application, simply execute the provided Python script. Ensure that you have Python 3.x and the PyQt6 library installed.