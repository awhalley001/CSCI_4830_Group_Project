import mysql.connector
import pandas
import csv
from hump_timer import TimeClass


def get_track_csv():
    '''Get tracks from user uploaded csv'''
    pass


def connect_to_database():
    '''Connect to local database'''
    pass


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


#_________---------------______________-----------------________________-----------_______
#_________---------------______________-----------------________________-----------_______


def connect_to_database():
    '''Connect to local database'''
    #TODO connect to aws via django
    mydb = mysql.connector.connect(
        auth_plugin="mysql_native_password",
        host="localhost",
        user="root",
        password="jollyStarter22",
        database="yardTracks"
    )
    if mydb:
        return mydb
    else:
        exit("Problem connecting to db")


def get_incoming_cars_id(cardata):
    '''Get the user uploaded csv file that includes the cars that need to be moved'''
    # "id" or "EQUIPMENT_NUMBER"
    cars = cardata["id"]
    return


def get_incoming_cars_track():
    '''Get the respective tracks for each of the incoming cars.'''
    pass


def get_cars_csv(fn):
    '''Get the cars csv from database.'''
    df = pandas.read_csv(fn)
    return df


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
    cardata = get_cars_csv("CAR_DATA1.csv")
    db = connect_to_database()
    cursor = db.cursor()

    # Example of sql statement execution
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)


    #get_track_csv()
    car_ids = get_incoming_cars_id(cardata)
    car_tracks = get_incoming_cars_track()

    #for x in range(len(car_ids)):
    #    car = car_ids[x]
    #    to_track = car_tracks[x]
    #
    #    while is_track_full(to_track):
    #        to_track = car_tracks[x + 1]
    #
    #    run_hump_timer()
    #
    #    update_track_capacity(to_track)
    #    update_car_location(car)

if __name__ == '__main__':
    main()
