"""This file acts as the main module for this script."""

import traceback
import adsk.core
import adsk.fusion
# import adsk.cam

# Initialize the global variables for the Application and UserInterface objects.
app = adsk.core.Application.get()
ui  = app.userInterface


def run(_context: str):
    """This function is called by Fusion when the script is run."""

    try:
        # Your code goes here.
        doc = app.activeDocument
        ui.messageBox(f"Hello, World!\nDocumento activo: {doc.name}")
    except Exception as e:  
        app.log(f'Error: {e}\nFailed to execute script.\n{traceback.format_exc()}')
