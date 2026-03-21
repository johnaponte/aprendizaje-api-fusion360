import adsk.core, adsk.fusion

def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    ui.messageBox("Hola Fusion 360")
