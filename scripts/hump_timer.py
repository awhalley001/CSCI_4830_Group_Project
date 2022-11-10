import time

def find_current_time():
    pass

def process_time_up():
    pass

def process_time_uncouple():
    pass

def process_time_down():
    pass

def if_track_same_as_previous():
    return True

def main():
    now_time = find_current_time()
    time_up = process_time_up(now_time)
    uncouple_time = process_time_uncouple(time_up)
    process_time_down(uncouple_time)

if __name__ == '__main__':
    main()