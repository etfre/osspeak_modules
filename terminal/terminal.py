from platforms.api import transcribe_line
import os
import tempfile

def drop(self, num):
    num = osspeak_queue.get(block=True)
    num = int(num)
    _, temp_name = tempfile.mkstemp()
    results =transcribe_line('ls > {}'.format(temp_name) + '{enter}')
    time.sleep(.5)
    try:
        with open(temp_name) as f:
            for i, line in enumerate(f, start=1):
                if i == num:
                   transcribe_line('cd {}'.format(line.rstrip('\n')) + '{enter}')
                    break
    finally:
        if os.path.isfile(temp_name):
    os.remove(temp_name)

drop()