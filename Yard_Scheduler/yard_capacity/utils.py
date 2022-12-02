from django.http import QueryDict
import json
from rest_framework import parsers
import mysql.connector


def handle_uploaded_file(f):
    with open('/home/adamhalley/github/CSCI_4830_Group_Project/scripts/CAR_SAMPLE.CSV', 'wb+') as destination:
        for chunk in f.chunks():
            print(chunk)
            destination.write(chunk)


class MultipartJsonParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}
        # find the data field and parse it
        data = json.loads(result.data["data"])
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return parsers.DataAndFiles(qdict, result.files)

class DbClass:
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

    def providetrackstable(self):
        # SHOW TABLE FOR TESTING
        table = []
        self.cursor.execute("SELECT * FROM testYard")
        for x in self.cursor:
            table.append(x)
        return table

    def providecarstable(self):
        # SHOW TABLE FOR TESTING
        table = []
        self.cursor.execute("SELECT * FROM testCars")
        for x in self.cursor:
            table.append(x)
        return table
