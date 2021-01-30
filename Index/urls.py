from django.urls import path, include

from Index import views

app_name = "Index"

urlpatterns = [
    path('', views.index.as_view() ,name="index"),  
    path('RecomendationWrite/', views.RecomendationWrite.as_view() ,name="RecomendationWrite"),  
    path('Contact/', views.Contact.as_view() ,name="Contact"),  
    path('AllProjects/', views.AllProjects.as_view() ,name="AllProjects"),  
    
   
    
]