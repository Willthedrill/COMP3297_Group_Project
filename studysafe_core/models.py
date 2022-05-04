
from django.db import models

#Create Models for storing information in studysafe core



class MemberRecord(models.Model):
    '''
    Record the member of HKU with hkuid  and name
    '''
    hkuid = models.CharField(max_length = 10,primary_key=True)
    name = models.CharField(max_length = 150)
    def __str__(self):
        return f'{self.hkuid},{self.name}'


class VenueRecord(models.Model):
    '''
    Record the Venues avaialble in the campus with venue_code, location, type and capacity. 
    '''
    type_choices={}
    venue_code=models.CharField(max_length=20,primary_key=True)
    location=models.CharField(max_length=150)
    type=models.CharField(max_length=2)
    capacity=models.IntegerField()
    def __str__(self):
        return f"## {self.venue_code}/{self.location}/{self.type}/{self.capacity} ##"

class Record(models.Model):
    '''
    Record the entry and exit record of individual student to/from individual venues. 
    '''
    hkuid = models.ForeignKey(MemberRecord,on_delete=models.CASCADE)
    venue_code = models.ForeignKey(VenueRecord,on_delete=models.CASCADE)
    datetime = models.CharField(max_length=30)
    # EN - enter ; EX - exit
    type = models.CharField(max_length=2)
    def __str__(self):
        newline='\n'
        return f'## {self.hkuid}/{self.venue_code}/{self.datetime}/{self.type} ##'