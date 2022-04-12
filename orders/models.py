from django.db import models

# Create your models here.
class MemberRecord(models.Model):
    uid = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.UID
    
    
class Record(models.model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)  # to be edited
    venue = models.CharField(max_length=10)
    datetime = models.DateTimeField()
