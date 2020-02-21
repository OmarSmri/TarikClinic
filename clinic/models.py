from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    height = models.FloatField(verbose_name='Height', blank=True, null=True)
    weight = models.FloatField(verbose_name='Weight', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Date Of Birth', blank=True, null=True)
    history = models.CharField(max_length=10000, blank=False, null=False)
    physical_examination = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
