from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Dietitian', 'Dietitian'),
    ('Endocrinology', 'Endocrinology'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
    ('Neurology', 'Neurology'),
    ('Gynaecology', 'Gynaecology'),
    ('Pediatrics', 'Pediatrics'),
    ('Ophthalmology', 'Ophthalmology'),
    ('Orthopedic', 'Orthopedic'),
    ('Pulmonologist','Pulmonologist'),
    ('Radiologist','Radiologist'),
    ('General Surgeon','General Surgeon')
)


class doctor(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='healthApp/images')
    description=models.TextField(default="")
    address = models.CharField(max_length=100,default="")
    shift_start_time = models.CharField(max_length=10)
    shift_end_time = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=100)
    nmc_number = models.CharField(max_length=10, default="")
    education_training = models.TextField(default="")
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    professional_experience = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name


class consultationform(models.Model):
    consult_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=30,default="")
    department =models.CharField(max_length=100,default="")
    date = models.CharField(max_length=50,default="")
    time = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50,default="")
    state =models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name
    