from django.db import models
from django.urls import reverse
from pyexpat import model
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    duration=models.IntegerField(blank=True)

    def get_url(self):
        return reverse('detailapp:detail',args=[self.id])

    def __str__(self):
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    desc=models.TextField(blank=True)
    def get_url(self):
        return reverse('detailapp:detail', args=[self.department.id, self.id])

def __str__(self):
    return self.name
class Student(models.Model):
    name=models.CharField(max_length=250,unique=True)
    DOB=models.DateField (max_length=250,blank=True)
    age = models.IntegerField(blank=True)
    gender=models.CharField(max_length=250,blank=True)
    phone_number=models.CharField(max_length=250,blank=True)
    email_id=models.EmailField()
    address=models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose_choices = (('enquiry', 'ENQUIRY'),
                          ('commerce', 'PLACEORDER'),
                          ('return', 'RETURN'),
                          )
    purpose = models.CharField(max_length=20, choices=purpose_choices)
    def __str(self):
        return self.name



















