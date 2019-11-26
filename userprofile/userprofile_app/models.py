from django.db import models

class User_Profile(models.Model):

    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.EmailField()
    display_picture = models.FileField()

    def __str__(self):
        return self.fname

