from django.db import models

 
 
class Student(models.Model):
    name=models.CharField(max_length=90)
    age=models.IntegerField()
    description=models.TextField()
    date_enrolled=models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.name 