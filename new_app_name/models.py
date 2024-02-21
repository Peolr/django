from django.db import models

class my_table_new(models.Model):
    column1 = models.CharField(max_length=200)
    column2 = models.IntegerField()

    class Meta:
        app_label = 'new_app_name'