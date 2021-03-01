# import concurrent.futures
import asyncio as aio

import multiprocessing
# import asyncio as aio
from attendance_main_windows import Main_activity as backend
from attendance_main_windows import Main_activity_gui as frontend

# async def start_two_files

if __name__ == "__main__":


    backend = multiprocessing.Process(target=backend.read_in_rfid_values)
    frontend = multiprocessing.Process(target=frontend.run_gui_program)
    #todo: the front end module should return a value i.e. true when the timer is counting down
    # and this should automaticall start the backend. when the timer is stopped the backend is shut down
    # frontend.

    frontend.start()
    backend.start()
    backend.join()
    frontend.join()