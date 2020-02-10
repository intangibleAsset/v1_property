from django.db import models
from django.conf import settings

# Create your models here.

class PropertyGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    property_reference = models.CharField(max_length=20, null=True, blank=True, unique=True)
    subject_surname = models.CharField(max_length=30, null=True, blank=True)
    group_ID = models.CharField(max_length=30, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property_reference

class PropertyItem(models.Model):
    property_group = models.ForeignKey(PropertyGroup, on_delete=models.SET_NULL,blank=True, null=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    seized_by = models.CharField(max_length=35, null=False, blank=False)
    seized_time = models.TimeField(null=False, blank=False)
    seized_date = models.DateField(null=False, blank=False)
    sub_location = models.CharField(max_length=80, null=False, blank=False)
    exhibit_reference = models.CharField(max_length=20, null=False, blank=False)
    notes = models.CharField(max_length=2000, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Owner(models.Model):
    property_item = models.ForeignKey(PropertyItem, on_delete=models.SET_NULL,blank=True, null=True)
    company = models.CharField(max_length=35, null=True, blank=True)
    first_name = models.CharField(max_length=35, null=True, blank=True)
    last_name = models.CharField(max_length=35, null=True, blank=True)
    date_of_birth = models.DateField(max_length=35, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name

class OwnerAddress(models.Model):
    property_item = models.ForeignKey(PropertyItem, on_delete=models.SET_NULL,blank=True, null=True)
    flat_number = models.CharField(max_length=10, null=True, blank=True)
    house_number = models.CharField(max_length=10, null=True, blank=True)
    house_name = models.CharField(max_length=50, null=True, blank=True)
    road_name = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.road_name

class FoundAddress(models.Model):
    property_group = models.ForeignKey(PropertyGroup, on_delete=models.SET_NULL,blank=True, null=True)
    flat_number = models.CharField(max_length=10, null=True, blank=True)
    house_number = models.CharField(max_length=10, null=True, blank=True)
    house_name = models.CharField(max_length=50, null=True, blank=True)
    road_name = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postcode


class FoundLocation(models.Model):
    property_group = models.ForeignKey(PropertyGroup, on_delete=models.SET_NULL,blank=True, null=True)
    word_one = models.CharField(max_length=80, null=True, blank=True)
    word_two = models.CharField(max_length=80, null=True, blank=True)
    word_three = models.CharField(max_length=80, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_time)

class SealNumber(models.Model):
    property_item = models.ForeignKey(PropertyItem, on_delete=models.SET_NULL,blank=True, null=True)
    seal_reference = models.CharField(max_length=80, null=True, blank=True, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.seal_reference:
            return self.seal_reference
        else:
            return 'No seal number'

class StoredLocation(models.Model):
    property_item = models.ForeignKey(PropertyItem, on_delete=models.SET_NULL,blank=True, null=True)
    current_location = models.CharField(max_length=80, null=False, blank=False, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.current_location

class PropertyItemImage(models.Model):
    property_item = models.ForeignKey(PropertyItem, on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField(null=True, blank=True, verbose_name="add image")
    image_number = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        if self.image.url:
            return str(self.image.url)
        else:
            return 'no image'
