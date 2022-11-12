import mysql
import csv
from timer.py import TimeClass


def get_track_csv():
    '''Get tracks from user uploaded csv'''
    pass

def connect_to_database():
    '''Connect to local database'''
    #TODO connect to aws via django

def import_csv_to_table():
    '''Use csv contents to populate table in database'''
    pass
 
def parse_cars_by_track():
    '''Add cars to track dictionary where Key=Trackname Value=Carnumber '''
    pass
    
def run_hump_timer():
    '''execute hump timer to time car movement into track and update track capacity'''
    pass
    
def update_track_capacity():
    '''update capacity column in database depending on where the cars are going'''
    pass

def is_track_full():
    '''Return if a track is full'''
    pass
    
def try_next_track():
    '''Search for nearest track to move overfill from previous track'''
    pass

'''----------------------------------------------------------------------'''

def connect_to_database():
    '''Connect to local database'''
    #TODO connect to aws via django

def get_incoming_cars_id():
    '''Get the user uploaded csv file that includes the cars that need to be moved'''
    pass

def get_incoming_cars_track():
    '''Get the respective tracks for each of the incoming cars.'''
    pass

def get_cars_csv():
    '''Get the cars csv from database.'''
    pass

def get_track_csv():
    '''Get the tracks csv from database.'''
    pass

def is_track_full():
    '''Returns true if the track is full. Returns false otherwise.'''
    pass

def run_hump_timer():
    '''Execute hump timer to time car mocement into track and update track capacity.'''
    pass

def update_track_capacity():
    '''Update the capacity column of the given track in the database.'''
    pass

def update_car_location():
    '''Update the location column of the given car in the database.'''
    pass

def main():
    connect_to_database()
    get_cars_csv()
    get_track_csv()
    car_ids = get_incoming_cars_id()
    car_tracks = get_incoming_cars_track()

    for x in range(len(car_ids)):
        car = car_ids[x]
        to_track = car_tracks[x]

        while is_track_full(to_track):
            to_track = car_tracks[x + 1]

        run_hump_timer()

        update_track_capacity(to_track)
        update_car_location(car)
    
if __name__ == '__main__':
    main()
