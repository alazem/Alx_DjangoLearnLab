from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
class student(models.Model):
    name= models.CharField(max_length=100)
class department(models.Model):
    name = models.CharField(max_length= 100)
    student = models.ForeignKey(student, on_delete=models.CASCADE, related_name='department')
    