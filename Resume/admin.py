from django.contrib import admin
from .models import Detail, School, Intermediate, Graduation, UiApplication, Contact, Project, Skills, Workexperience

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1  # How many rows to show
    

class UiApplicationInline(admin.TabularInline):
    model = UiApplication
    extra = 1  # How many rows to show
    

class SchoolInline(admin.TabularInline):
    model = School
    max_num=1

class IntermediateInline(admin.TabularInline):
    model = Intermediate
    max_num=1
    
class GraduationInline(admin.TabularInline):
    model = Graduation
    max_num=1

   
class SkillsInline(admin.TabularInline):
    model = Skills
    extra=1
  
class WorkexperienceInline(admin.TabularInline):
    model = Workexperience
    extra=1

class DetailAdmin(admin.ModelAdmin):
    inlines = [ProjectInline, UiApplicationInline, SchoolInline, IntermediateInline, GraduationInline, SkillsInline, WorkexperienceInline]

# Register your models here.
admin.site.register(Detail, DetailAdmin)
admin.site.register(School)
admin.site.register(Intermediate)
admin.site.register(Contact)
admin.site.register(Graduation)
