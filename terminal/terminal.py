from platforms.api import type_line
import time
import os
import tempfile

def drop():
    num = osspeak_queue.get(block=True)
    num = int(num)
    _, temp_name = tempfile.mkstemp()
    results = type_line([f'ls > {temp_name}', ['enter']])
    time.sleep(.5)
    try:
        with open(temp_name) as f:
            for i, line in enumerate(f, start=1):
                if i == num:
                    line = line.rstrip("\n")
                    type_line([f'cd {line}', ['enter']])
                    break
    finally:
        if os.path.isfile(temp_name):
            os.remove(temp_name)

drop()