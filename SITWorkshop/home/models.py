from django.db import models

AI = 'AIML'
AD = 'AIDS'
IS = 'IS'
Branch = (
    (AI, "AI"),
    (AD, "AD"),
    (IS, "IS")
)
# Create your models here.
class register(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.BigIntegerField()
    Usn = models.CharField(max_length=15)
   # sem = models.CharField(max_length=10,choices = sem,default='useless',null=True)
    Email = models.CharField(max_length=100)
    Branch = models.CharField(max_length=10, choices=Branch,default='useless')
    Laptop = models.BooleanField()
    date = models.DateField()
    def __str__(self):
        return self.Name
