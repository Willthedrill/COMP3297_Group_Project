from django.db import models

# Create your models here.
class MemberRecord(models.Model):
    uid = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.UID