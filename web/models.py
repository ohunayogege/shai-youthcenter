from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(_('Name'), max_length=200, default='')
    slug = models.SlugField()
    status = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class YouthForm(models.Model):
    RESIDE = (
        ('Own', 'Own'),
        ('Parents', 'Parents'),
        ('Spouse', 'Spouse'),
        ('Partners', 'Partners'),
        ('Hostel & Sheltered Housing', 'Hostel & Sheltered Housing'),
        ('Other', 'Other')
    )
    MARITAL = (
        ('Single', 'Single'),
        ('Significant Relationship', 'Significant Relationship'),
        ('Known in public', 'Known in public'),
        ('Married', 'Married'),
        ('Seperated', 'Seperated'),
        ('Divorced', 'Divorced'),
        ('Widower', 'Widower')
    )
    yid = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, default='')
    first_name = models.CharField(_('First Name'), max_length=100, default='')
    last_name = models.CharField(_('Last Name'), max_length=100, default='')
    mobile_no = models.CharField(_('Cell Phone'), max_length=100, default='')
    phone_no = models.CharField(_('Cell Phone'), max_length=100, default='', blank=True)
    dob = models.DateField(auto_now_add=False)
    house_no = models.PositiveIntegerField(default=0)
    street = models.TextField(_('Street Address'), default='')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, default='')
    residence = models.CharField(_('Residence'), max_length=100, choices=RESIDE, default='')
    other_res = models.CharField(_('Other Resident'), max_length=400, default='', blank=True)
    country_of_birth = models.CharField(_('Country of Birth'), max_length=100, default='')
    year_immigration = models.CharField(_('Year of Immigration'), max_length=10, default='', blank=True)
    marital_status = models.CharField(_('Marital Status'), max_length=100, choices=MARITAL, default='')
    children = models.BooleanField(default=False)
    no_of_children = models.PositiveIntegerField(default=0)
    languages = models.CharField(max_length=400, default='')
    driver_license = models.BooleanField(_('Holder of Driver License'), default=False)
    reasons = models.TextField(default='')
    work_exp = models.BooleanField(_('Working Experience?'), default=False)
    current_job = models.CharField(_('Current Job'), max_length=100, default='', blank=True)
    role = models.CharField(_('Job Role'), max_length=100, default='', blank=True)
    study_framework = models.TextField(default='')
    place_of_study = models.CharField(max_length=100, default='', blank=True)
    graduate_year = models.CharField(max_length=100, default='', blank=True)
    years_of_education = models.CharField(max_length=100, default='')
    academy_level = models.CharField(max_length=100, default='')
    military_national_service = models.CharField(max_length=100, default='', blank=True)
    duration_service = models.CharField(max_length=100, default='', blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Newsletter(models.Model):
    email = models.EmailField(max_length=200, default='')
    first_name = models.CharField(_('First Name'), max_length=100, default='')
    last_name = models.CharField(_('Last Name'), max_length=100, default='')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
