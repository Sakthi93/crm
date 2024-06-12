from django.contrib.auth.models import User
from django.db import models

class leads(models.Model):
    New ='new'
    Inprogress ='inprogress'
    Lost ='lost'
    Won = 'won'
    CHOICES_STATUS = {
        ( New ,'new'),
        (Inprogress ,'inprogress'),
        (Lost ,'lost'),
        (Won ,'won')
        
    }
    
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email =models.EmailField()
    phone = models.IntegerField()
    website = models.CharField(max_length=255,blank= 'true' ,null= 'true')
    confidence = models.IntegerField(blank= 'true' ,null= 'true')
    estimated_value = models.IntegerField(blank= 'true' ,null= 'true')
    status = models.CharField(max_length=25,choices=CHOICES_STATUS,default=New)
    created_by = models.ForeignKey(User, related_name= 'leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    
    
    

