from django.db import models
from datetime import datetime
import time
import uuid
# Create your models here.

class PersonalInfo(models.Model):
    Pi_custom_id        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image               = models.ImageField(upload_to="PersonalInfo/OwnerImage",)
    Resume              = models.FileField(upload_to="PersonalInfo/OwnerResume",)
    Name                = models.CharField(max_length=250)
    TagLine             = models.CharField(max_length=250)
    PhoneNumber         = models.CharField(max_length=250)
    Email               = models.CharField(max_length=250)


    def __str__(self):
        return self.Name





class Recomendations(models.Model):
    Recom_custom_id         = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Name                    = models.CharField(max_length=250)
    CompanyName             = models.CharField(max_length=500)
    Designation             = models.CharField(max_length=500)
    Email                   = models.CharField(max_length=500, default='self')
    RecomendationMsg        = models.CharField(max_length=50000)
    date                    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name



class TechStack(models.Model):
    Stack_custom_id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    StackName                       = models.CharField(max_length=250)
    Star1                           = models.BooleanField(default=False)
    Star2                           = models.BooleanField(default=False)
    Star3                           = models.BooleanField(default=False)
    Star4                           = models.BooleanField(default=False)
    Star5                           = models.BooleanField(default=False)
    Star6                           = models.BooleanField(default=False)
    image                           = models.ImageField(upload_to="TechImage")


    def __str__(self):
        return self.StackName




class Project(models.Model):
    Project_custom_id                   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProjectName                         = models.CharField(max_length=250)
    ProjectLink                         = models.CharField(max_length=1000)
    ProjectDescribtion                  = models.CharField(max_length=50000)
    image                               = models.ImageField(upload_to="ProjectImage")
    


    def __str__(self):
        return self.ProjectName


class AboutMe(models.Model):
    about_custom_id                 = models.UUIDField(primary_key=True,default=uuid.uuid4,  editable=False)
    TagLine                         = models.CharField(max_length=250)
    What_can_i_do                   = models.CharField(max_length=5000, default='self')
    What_am_i_doing_currently       = models.CharField(max_length=5000, default='self')
    What_do_i_belive_in             = models.CharField(max_length=5000, default='self')
    How_i_can_help_you              = models.CharField(max_length=5000, default='self')


    def __str__(self):
        return str(self.about_custom_id)


class Education(models.Model):
    edu_custom_id           = models.UUIDField(primary_key=True,default=uuid.uuid4,  editable=False)
    NameOfInstitute         = models.CharField(max_length=250)
    NameOfDegree            = models.CharField(max_length=250)
    StartToEndDate          = models.CharField(max_length=250)
   

    def __str__(self):
        return str(self.NameOfInstitute)



class WorkExperience(models.Model):
    work_custom_id          = models.UUIDField(primary_key=True,default=uuid.uuid4,  editable=False)
    NameOfCompany           = models.CharField(max_length=250)
    NameOfPost              = models.CharField(max_length=250)
    StartToEndDate          = models.CharField(max_length=250)
 



    def __str__(self):
        return str(self.NameOfCompany)



class ContactUs(models.Model):
    Contact_custom_id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name                        = models.CharField(max_length=250)
    Email                       = models.CharField(max_length=500, default='self')
    ProjectMsg                  = models.CharField(max_length=50000)
    date                        = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.Name
