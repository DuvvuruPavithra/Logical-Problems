import time


def stop_watch():
    start_time = input("Press Enter the start time :")
    starting_point = time.time()
    end_time = input("Press Enter to stop time :")
    ending_point = time.time()
    elapsed_time = ending_point - starting_point
    print("Total elapsed time is : ", elapsed_time)
stop_watch()

