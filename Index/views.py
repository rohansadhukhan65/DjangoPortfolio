from django.shortcuts import *
from django.views.generic import *

from Index.models import *

# Email configuration
from django.conf import settings
from django.core.mail import send_mail
# Email configuration end




# Create your views here.


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        Personal_Info = PersonalInfo.objects.all().first()
        Recomendation = Recomendations.objects.all().order_by('?')
        stack = TechStack.objects.all().order_by('?')
        Projects = Project.objects.all().order_by('?')
        About = AboutMe.objects.all()
        educat = Education.objects.filter()[::-1]
        work= WorkExperience.objects.all()

        context = {
            'PersonalInfo': Personal_Info,
            'recomend': Recomendation,
            'project': Projects,
            'Tstack': stack,
            'about': About,
            'education': educat,
            'workexp': work
        }
        return context



class RecomendationWrite(TemplateView):
    template_name = 'Recomendation.html'

    def get_context_data(self, **kwargs):
        Personal_Info = PersonalInfo.objects.all().first()
        Recomendation = Recomendations.objects.all()
        Projects = Project.objects.all()

        context= {'PersonalInfo':Personal_Info,'recomend':Recomendation,'project':Projects,}
        return context

    def post(self, request, *args, **kwargs):
        if 'name' in request.POST:
            Name = request.POST['name']

            if 'email' in request.POST:
                Email = request.POST['email']

            if 'Company_Institution' in request.POST:
                CompanyInstitution = request.POST['Company_Institution']

            if 'Designation' in request.POST:
                designation = request.POST['Designation']

            if 'Recomendation' in request.POST:
                recomendation = request.POST['Recomendation']

                reco = Recomendations.objects.update_or_create(Name=Name,
                                                            CompanyName=CompanyInstitution,
                                                            Designation=designation,
                                                            Email=Email
                                                            , defaults={'Name': Name,
                                                                        'CompanyName': CompanyInstitution,
                                                                        'Designation': designation,
                                                                        'Email': Email,
                                                                        'RecomendationMsg': recomendation,})




        return redirect('Index:index')


class Contact(TemplateView):
    template_name = 'Contact.html'

    def get_context_data(self, **kwargs):
        Personal_Info = PersonalInfo.objects.all().first()
        Recomendation = Recomendations.objects.all()
        Projects = Project.objects.all()

        context= {'PersonalInfo':Personal_Info,'recomend':Recomendation,'project':Projects,}
        return context



    def post(self, request, *args, **kwargs):
        if 'name' in request.POST:
            Name = request.POST['name']

            if 'email' in request.POST:
                Email = request.POST['email']


            if 'Projectmsg' in request.POST:
                projectmsg = request.POST['Projectmsg']

                Promsg = ContactUs(
                    Name=Name,
                    Email=Email,
                    ProjectMsg= projectmsg,
                   )
                Promsg.save()

                subject = f'New Project Request From Your Portfolio ! by {Name.split()[0]} '
                message = projectmsg
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['sadhukhanrohan15@gmail.com' ]
                send_mail( subject, message, email_from, recipient_list )


        return redirect('Index:index')



class AllProjects(TemplateView):
    template_name = 'All_projects.html'

    def get_context_data(self, **kwargs):
       
        Projects = Project.objects.all().order_by('?')
        
        

        context = {
           
            'project': Projects,
        
         
        }
        return context
