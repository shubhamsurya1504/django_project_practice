from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

TYPE = (
    ('MECH', 'MECH-Type'),
    ('ELECTRICAL', 'ELECTRICAL-Type'),
    ('CHEM', 'Chemical-Type'),
    ('IT', 'IT-Type'),
    ('ROBOTICS', 'Robotics-Type')
)

STAGE = (
    ('0-25 Percent', '0-25 Percent'),
    ('25-50 Percent', '25-50 Percent'),
    ('50-75 Percent', '50-75 Percent'),
    ('75-99 Percent', '75-99 Percent'),
    ('100 Percent', '100 Percent--'),
)


class Country(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=30)
    #
    # @property
    def __str__(self):
        return self.country_name


class City(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,
    #                          blank=True, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    city_name = models.CharField(max_length=300, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    #
    def __str__(self):
        return '%s -%s' % (self.country, self.city_name)


class Fees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
#    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fees_date = models.DateTimeField()
    total_amount = models.IntegerField()
    balance_amount = models.IntegerField()
    course_name = models.CharField(max_length=70)
    level = models.CharField(max_length=70)
    

    def __str__(self):
        return '%s -%s' % (self.course_name, self.level)


class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    course_name = models.CharField(max_length=300, null=True, blank=True)
    level = models.CharField(max_length=300, null=True, blank=True)
    fees = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.course_name, self.level)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.SET_NULL)
    student_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    fees_name = models.ForeignKey(Fees, on_delete=models.CASCADE)
    fees_paid = models.IntegerField()
    #courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    branch = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

    def __str__(self):
        return '%s --%s' % (self.user,self.student_name)

    class Meta:
        verbose_name = "Students Information"
        verbose_name_plural = "Students Informations"
    



  
