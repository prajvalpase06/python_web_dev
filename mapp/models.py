from django.db import models

# Create your models here.

# makemigrations - create changes and store in the file
# migrate - apply changes made a makemigrations

class Contact(models.Model):
    serialNumber = models.TextField()
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        # return ("Name: " + self.name + "\nEmail: " + self.email) 
        return self.name
