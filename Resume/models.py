from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=255, default=None)
    preview_image1 = models.ImageField(upload_to="images/", default=None)
    preview_image2 = models.ImageField(upload_to="images/", default=None)
    
    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=255, default=None)
    marks = models.CharField(max_length=255, default=None)
    duration = models.DateField(default=None)
    location = models.TextField(max_length=255, default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="school")
    
    def __str__(self):
        return f"{self.name}, {self.marks}, {self.duration}, {self.location}"

class Intermediate(models.Model):
    name = models.CharField(max_length=255, default=None)
    duration_from = models.DateField(default=None)
    duration_to = models.DateField(default=None)
    marks = models.CharField(max_length=255, default=None)
    location = models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="intermediate")
    
    def __str__(self):
        return f"{self.name}, {self.duration_from}, {self.duration_to}, {self.marks}, {self.location}"
    
class Graduation(models.Model):
    name = models.CharField(max_length=255, default=None)
    duration_from = models.DateField(default=None)
    duration_to = models.DateField(default=None)
    marks = models.CharField(max_length=255, default=None)
    location = models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="graduation")
    
    def __str__(self):
        return f"{self.name}, {self.duration_from}, {self.duration_to}, {self.marks}, {self.location}"


class Project(models.Model):
    title = models.CharField(max_length=255, default=None)
    duration_from = models.DateField(default=None)
    duration_to = models.DateField(default=None)
    description = models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="projects")
    
    def __str__(self):
        return f"{self.title}, {self.duration_from}, {self.duration_to}, {self.description}"

class UiApplication(models.Model):
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    technologies = models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="ui_applications")
    
    def __str__(self):
        return f"{self.title}, {self.description}, {self.technologies}"

class Contact(models.Model):
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=15, default=None)
    github = models.CharField(max_length=255, default=None)
    linkedin = models.CharField(max_length=255, default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="contacts")
    
    def __str__(self):
        return f"{self.email}, {self.phone_number}, {self.github}, {self.linkedin}"

class Skills(models.Model):
    skill=models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="skills")
    
    def __str__(self):
        return self.skill

class Workexperience(models.Model):
    title = models.CharField(max_length=255, default=None)
    company_name=models.CharField(default=None)
    duration_from = models.DateField(default=None)
    duration_to = models.DateField(default=None)
    description = models.TextField(default=None)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name="experience")
    
    def __str__(self):
        return f"{self.title},{self.company_name}, {self.duration_from}, {self.duration_to}, {self.description}"
    