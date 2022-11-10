import datetime
import time


class TimeClass:
    def __init__(self):
        self.dateTimeObject = datetime.datetime.now()
        self.showTime = None
        self.timestring()

    def timestring(self):
        self.showTime = self.dateTimeObject.strftime("%X")


def find_current_time():
    x = datetime.datetime.now()
    return x


def process_time_up(start_time):
    shove_up_hump_time_minutes = 2
    final_time = start_time + datetime.timedelta(minutes=shove_up_hump_time_minutes)
    seconds = int((final_time-start_time).total_seconds())
    time.sleep(seconds)
    return final_time


def process_time_uncouple(start_time):
    uncouple_cars_time_minutes = 2
    final_time = start_time + datetime.timedelta(minutes=uncouple_cars_time_minutes)
    seconds = int((final_time-start_time).total_seconds())
    time.sleep(seconds)
    return final_time


def process_time_down(start_time):
    down_the_hump_time_minutes = 2
    final_time = start_time + datetime.timedelta(minutes=down_the_hump_time_minutes)
    seconds = int((final_time-start_time).total_seconds())
    time.sleep(seconds)
    return final_time


def if_track_same_as_previous():
    return True


def main():
    t = TimeClass()
    now_time = t.dateTimeObject

    time_up = process_time_up(now_time)

    uncouple_time = process_time_uncouple(time_up)

    process_time_down(uncouple_time)


if __name__ == '__main__':
    main()