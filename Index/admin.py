from django.contrib import admin

from Index.models import *
# Register your models here.


class personalInfo(admin.ModelAdmin):
    list_display = ( 'image','Name',   'TagLine','PhoneNumber', 'Email')


class techStack(admin.ModelAdmin):
    list_display = ( 'StackName','Star1','Star2','Star3','Star4','Star5', 'Star6', 'image')

class project(admin.ModelAdmin):
    list_display = ( 'ProjectName','ProjectLink',   'ProjectDescribtion','image')

class  recomendations(admin.ModelAdmin):
    list_display = (  'Name', 'RecomendationMsg', 'Email','CompanyName', 'Designation','date')


class  contactUs(admin.ModelAdmin):
    list_display = (  'Name', 'Email', 'ProjectMsg','date')



class aboutMe(admin.ModelAdmin):
    list_display = ( 'TagLine','What_can_i_do','What_am_i_doing_currently','What_do_i_belive_in','How_i_can_help_you' )


class education(admin.ModelAdmin):
    list_display = (  'NameOfInstitute','NameOfDegree','StartToEndDate')



class workExperience(admin.ModelAdmin):
    list_display = ('work_custom_id', 'NameOfCompany', 'NameOfPost',
                    'StartToEndDate')




admin.site.register(PersonalInfo , personalInfo)
admin.site.register(TechStack , techStack)
admin.site.register(Project , project)
admin.site.register(Recomendations , recomendations)
admin.site.register(ContactUs, contactUs)
admin.site.register(AboutMe, aboutMe)
admin.site.register(Education, education)
admin.site.register(WorkExperience, workExperience)
