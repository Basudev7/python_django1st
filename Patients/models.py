from django.db import models

# Create your models here.
class Patient(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('close', 'Close'),
    )

    STAGE_CHOICES = {
        ('enquiry',"Enquiry"),
        ('contacted',"Contacted"),
        ('confirmed',"Confirmed"),
        ('cancelled',"Cancelled"),
        ('landed',"Landed"),
        ('treatment_in_process',"Treatment in Process"),
        ('succesfully_treated',"Successfully Treated"),
        ('money_in_the_bank','Money In The Bank')
    }
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    stage = models.CharField(max_length=50,choices=STAGE_CHOICES, default='enquiry')
    # timestamp = models.DateTimeField(auto_now_add=True)
    # last_updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.name}'