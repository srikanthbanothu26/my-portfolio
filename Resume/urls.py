from django.urls import path
from Resume.views import overview, education, Skills, Projects, Uiapplications, Workexperience, Contact
urlpatterns=[path("", overview , name="home"),
             path("education/", education, name="education"),
             path("Skills/", Skills, name="skills"),
             path("Projects/", Projects, name="projects"),
             path("Uiapplications/", Uiapplications, name="uiapplications"),
             path("Workexperience/", Workexperience, name="workexperience"),
             path("Contact/", Contact, name="contact"),
             
             ]