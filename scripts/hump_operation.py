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

def main():
    pass
    
if __name__ = '__main__':
    main()
