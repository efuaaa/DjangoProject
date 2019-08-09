from django.db import models

# Create your models here.
class profiles(models.Model):
    firstname = models.CharField(max_length=120, default = 'null') #max_length=120
    lastname = models.CharField(max_length=120, default = 'null') 
    gender = models.CharField(max_length=120, default = 'null') 
    dob = models.CharField(max_length=120, default = 'null') 
    callNumber = models.CharField(max_length=120, default = 'null') 
    whatsappNumber = models.CharField(max_length=120, default = 'null') 
    ministry = models.CharField(max_length=120, default = 'null') 
    centre = models.CharField(max_length=120, default = 'null') 
    campus = models.CharField(max_length=120, default = 'null') 
    hostel_address = models.CharField(max_length=120, default = 'null') 
    city = models.CharField(max_length=120, default = 'null') 
    qualification = models.CharField(max_length=120, default = 'null') 
    profession = models.CharField(max_length=120, default = 'null') 
    maritalStatus = models.CharField(max_length=120, default = 'null') 
    bacenta = models.CharField(max_length=120, default = 'Doctor') 
    layschool = models.CharField(max_length=120, default = 'null') 
    imagefile = models.FileField(upload_to='images/', null=True, verbose_name="Image")


    
def __str__(self):
    return str(self.imagefile)
  