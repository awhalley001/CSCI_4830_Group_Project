import os
import mysql.connector
import pandas
import csv
import hump_timer

class dbClass:
    def __init__(self):
        self.db = mysql.connector.connect(
        auth_plugin="mysql_native_password",
        host="localhost",
        user="newuser",
        password="csci4830!",
        database="yardTracks"
    )
        self.cursor = self.db.cursor()
        # pandas df of testYard table in db
        self.dbyard = self.get_track_data()
        # pandas df of testCars table in db
        #self.dbcars = self.get_cars_data()

    def get_cars_data(self):
        pass
        '''Get the cars table from database.'''
        self.cursor.execute("SELECT id, EQUIPMENT_INITIAL, EQUIPMENT_NUMBER, CURRENT_YARD, CURRENT_TRAIN_DATE FROM testCars")
        df = pandas.DataFrame(self.cursor.fetchall())
        df.columns = ['id', 'EQUIPMENT_INITIAL', 'EQUIPMENT_NUMBER', 'CURRENT_YARD', 'CURRENT_TRAIN_DATE']
        return df

    def get_track_data(self):
        '''Get the tracks table from database.'''
        self.cursor.execute("SELECT id,SBDV_NAME,TRK_SYS_NBR,dist,car_capacity FROM testYard")
        df = pandas.DataFrame(self.cursor.fetchall())
        df.columns = ['id', 'SBDV_NAME', 'TRK_SYS_NBR', 'dist', 'car_capacity']
        return df

    def update_track_capacity(self, trackid):
        '''Update the capacity column of the given track in the database.'''

        currentcapacity = int(self.dbyard.loc[self.dbyard['id'] == trackid, 'car_capacity'])
        updatedcapacity = currentcapacity - 1
        # update df
        self.dbyard.loc[self.dbyard['id'] == trackid, ['car_capacity']] = updatedcapacity
        #print(self.dbyard)
        # update db
        self.cursor.execute("UPDATE testYard SET car_capacity =" + str(updatedcapacity) + " WHERE id = " + str(trackid))
        # commits changes to db
        self.db.commit()


    def update_car_location(self, car):
        '''Update the location column of the given car in the database.'''
        print("car data gets added to the dbcars dataframe and the db gets updated")
        # update df
        #self.dbcars.loc[len(self.dbcars.index)] = [car['id'], car['EQUIPMENT_INITIAL'], car['EQUIPMENT_NUMBER'],
                                        # car['CURRENT_YARD_CIRC7'], car['CURRENT_TRAIN_DATE']]
        # update db
        self.cursor.execute(
            "INSERT INTO testCars(EQUIPMENT_INITIAL, EQUIPMENT_NUMBER, CURRENT_YARD, CURRENT_TRAIN_DATE) VALUES (\'" +
            car['EQUIPMENT_INITIAL'] + "\',\'" + str(car['EQUIPMENT_NUMBER']) + "\',\'" + car[
                'CURRENT_YARD_CIRC7'] + "\',\'" + car['CURRENT_TRAIN_DATE'] + "\')")
        # commits changes to db
        self.db.commit()

    def showtable(self):
        # SHOW TABLE FOR TESTING
        self.cursor.execute("SELECT * FROM testCars")
        for x in self.cursor:
            print(x)

    def wipe(self):
        self.cursor.execute("TRUNCATE testCars")
        self.cursor.execute("UPDATE testYard SET car_capacity = 49")
        self.db.commit()


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
    # hump_timer.main()
    print("time passes")


def main():
    os.chdir("../")
    os.chdir("scripts/")
    numberoftracks=49
    # returns pandas df of car_data.txt file
    print(os.getcwd())
    uploadedcardata = get_cars_csv("CAR_SAMPLE.CSV")

    db = dbClass()
    db.wipe()
    db = dbClass()
    # returns column from yarddata dataframe
    car_tracks = get_incoming_cars_track(db.dbyard)

    for x in range(len(uploadedcardata.index)):
        db = dbClass()
        y=x%50
        car = uploadedcardata.iloc[x]

        to_track = car_tracks[y]

        while is_track_full(db.dbyard, y):
            to_track = car_tracks[y + 1]

        run_hump_timer()
        # updates the db and dataframe
        db.update_track_capacity(to_track)
        db.update_car_location(car)


if __name__ == '__main__':
    main()

