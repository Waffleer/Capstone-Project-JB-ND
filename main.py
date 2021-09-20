


import time
from datetime import datetime
import django


def start():
    global Timeo
    global now
    Timeo = time.perf_counter()
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Script Started at {dt}")
    print("\n\n")

def end():
    print(f"\n\nScript finished in {round(Timeo, 2)}\n\n")

start()
import django



print(django.get_version())






end()





