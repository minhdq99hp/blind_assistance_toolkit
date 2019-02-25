import pyxhook
import subprocess

def OnMouseEvent(event):
    x, y = event.Position

    # print('MessageName:',event.MessageName)
    # print('Window:',event.Window)
    # print('WindowName:',event.WindowName)
    # print('Position:',event.Position)
    # print('---')


    return True

new_hook = pyxhook.HookManager()
new_hook.MouseMovement = OnMouseEvent


new_hook.HookMouse()


try:
    new_hook.start()  # start the hook
except KeyboardInterrupt:
    # User cancelled from command line.
    pass
except Exception as ex:
    # Write exceptions to the log file, for analysis later.
    msg = 'Error while catching events:\n  {}'.format(ex)
    pyxhook.print_err(msg)
