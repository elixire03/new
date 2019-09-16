from django.db import models

# Create your models here.
class Craft(models.Model):
    description = models.CharField(max_length=100, unique=True)
    category = models.IntegerField()

    def __str__(self):
        return self.description

class Employees(models.Model):
    id_number=models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    emp_craft = models.ForeignKey(Craft,on_delete =models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    date_hired = models.DateTimeField()
    educational_attainment = models.CharField(max_length=200)
    passport_no = models.CharField(max_length=30)
    residencial_id = models.CharField(max_length=30)
    res_type = models.IntegerField()
    res_id_date_issued = models.DateField()
    res_id_date_expires = models.DateField()
    monthly_basic_salary = models.FloatField()
        
    def __str__(self):
        return self.id_number

class Service_record(models.Model):
    emp_id = models.ForeignKey(Employees,on_delete =models.CASCADE)
    emp_no = models.CharField(max_length=50)
    basic_salary = models.FloatField()
    date_of_service = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.emp_no