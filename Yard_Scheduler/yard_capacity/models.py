# Alexandria/catalog/models.py
from django.db import models


class Yard(models.Model):
    sbdv_name = models.CharField(max_length=30)
    trk_sys_nbr = models.IntegerField()
    dist = models.FloatField()
    car_capacity = models.IntegerField()

    def __str__(self):
        return f"Yard Name=({self.sbdv_name})"

    def get_track_system_number(self):
        return self.trk_sys_nbr

    def get_length_of_track_ft(self):
        return self.dist

    def get_track_car_capacity(self):
        return self.car_capacity

class Testyard(models.Model):
    sbdv_name = models.CharField(db_column='SBDV_NAME', max_length=30)  # Field name made lowercase.
    trk_sys_nbr = models.CharField(db_column='TRK_SYS_NBR', max_length=30)  # Field name made lowercase.
    dist = models.CharField(max_length=30)
    car_capacity = models.CharField(max_length=30)
    
    def __str__(self):
        return self.sbdv_name

    class Meta:
        managed = True
        db_table = 'testYard'

class Car(models.Model):
    equipment_initial = models.TextField()
    trk = models.IntegerField()
    equipment_number = models.IntegerField()
    current_yard_circ7 = models.CharField(max_length=(10))
    current_train_date = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Car being humped (id={self.id}, " \
               f"car number={self.equipment_initial} " \
               f"{self.equipment_number}, on track number {self.trk})"


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

class Posts(models.Model):
    equipment_initial = models.TextField()
    equipment_number = models.IntegerField()
    current_yard_circ_7 = models.IntegerField()
    current_train_date = models.TextField()
    dest_track = models.IntegerField()