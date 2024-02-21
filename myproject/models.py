from django.db import models

class MyTable(models.Model):
    # define your fields here
    column1 = models.CharField(max_length=200)
    column2 = models.CharField(max_length=200)
    class Meta:
        app_label = 'myproject'  # replace 'myapp' with the name of your application
        db_table = 'my_table'  # specify your actual table name here