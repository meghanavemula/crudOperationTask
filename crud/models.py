from django.db import models

# Create your models here.
class employee(models.Model):
    Full_name=models.CharField(max_length=50)
    Emial_id=models.CharField(max_length=100)
    Contact=models.CharField(max_length=50)


    class Meta:
        managed=False
        db_table='employee'