from django.db import models

# Create your models here.
class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def get_role():
        return "Staff:"
    
    class Meta:
        abstract = True
        
    class Manager(StaffBase):
        department = models.CharField(max_length=100)
        has_company_keycard = models.BooleanField(default=True)
        def get_role():
            return "Manager"
    
    class Intern(StaffBase):
        mentor = models.CharField(max_length=100, blank=True, null=True)
        start_date = models.DateField()
        def get_role():
            return "Intern"