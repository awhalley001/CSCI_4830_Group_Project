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


def get_cars_data(db):
    '''Get the cars table from database.'''
    cursor = db.cursor()
    cursor.execute("SELECT id, EQUIPMENT_INITIAL, EQUIPMENT_NUMBER, CURRENT_YARD, CURRENT_TRAIN_DATE FROM testCars")
    df = pandas.DataFrame(cursor.fetchall())
    df.columns=['id', 'EQUIPMENT_INITIAL', 'EQUIPMENT_NUMBER', 'CURRENT_YARD', 'CURRENT_TRAIN_DATE']
    return df


def get_track_data(db):
    '''Get the tracks table from database.'''
    cursor = db.cursor()
    cursor.execute("SELECT id,SBDV_NAME,TRK_SYS_NBR,dist,car_capacity FROM testYard")
    df = pandas.DataFrame(cursor.fetchall())
    df.columns=['id', 'SBDV_NAME', 'TRK_SYS_NBR', 'dist', 'car_capacity']
    return df


def get_incoming_cars_track(yarddata):
    '''Get the respective tracks for each of the incoming cars.'''
    # "id" or "TRK_SYS_NBR"
    tracks = yarddata["id"]
    return tracks


def get_cars_csv(filename):
    '''Get the cars csv from uploaded user file.'''
    df = pandas.read_csv(filename)
    return df


def is_track_full(dbyard,trackid):
    '''Returns true if the track is full. Returns false otherwise.'''

    if dbyard.at[trackid, 'car_capacity'] == 0:
        return True
    else:
        return False


def run_hump_timer():
    '''Execute hump timer to time car mocement into track and update track capacity.'''
    print("time passes")



def update_track_capacity(dbyard, trackid):
    '''Update the capacity column of the given track in the database.'''
    currentcapacity = int(dbyard.at[trackid, 'car_capacity'])
    print(dbyard.loc[[trackid]])
    dbyard.at[trackid, 'car_capacity'] = currentcapacity - 1
    print(dbyard.loc[[trackid]])

    #still need to update db
    ...
    return dbyard


def update_car_location(car, dbcars):
    '''Update the location column of the given car in the database.'''
    print("car data gets added to the dbcars dataframe and the db gets updated")
    pass


def main():
    #dataframe will be referred to as df

    # returns pandas df of car_data.txt file
    uploadedcardata = get_cars_csv("CAR_DATA1.csv")

    db = connect_to_database()
    # returns pandas df of testYard table in db
    dbyard = get_track_data(db)
    # returns pandas df of testCars table in db
    dbcars = get_cars_data(db)

    # returns column from yarddata dataframe
    car_tracks = get_incoming_cars_track(dbyard)

    for x in range(len(uploadedcardata.index)):
        car = uploadedcardata.iloc[x]
        to_track = car_tracks[x]

        while is_track_full(dbyard, to_track):
            to_track = car_tracks[x + 1]

        run_hump_timer()

        dbyard = update_track_capacity(dbyard, to_track)
        update_car_location(car, dbcars)

if __name__ == '__main__':
    main()
