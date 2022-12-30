from django.db import models

# Create your models here.
class deptmodel(models.Model):
    dep_name=models.CharField(max_length=255)
    dep_desc=models.TextField()

    def __str__(self):
        return self.dep_name

class doctorsmodel(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(deptmodel,on_delete=models.CASCADE,null=True,blank=True)
    doc_image=models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name

class bookingmodel(models.Model):
   p_name=models.CharField(max_length=255)
   p_phone=models.CharField(max_length=10)
   p_email=models.EmailField()
   doc_name=models.ForeignKey(doctorsmodel,on_delete=models.CASCADE)
   booking_date=models.DateField()
   booked_on=models.DateField(auto_now=True)

class signupmodel(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.IntegerField()
    email = models.EmailField()
    password=models.CharField(max_length=10)
    re_password=models.CharField(max_length=10)

