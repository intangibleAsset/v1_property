from django.contrib import admin


from . models import PropertyItemImage, FoundAddress, PropertyGroup, PropertyItem, OwnerAddress, FoundLocation, SealNumber, StoredLocation, Owner
# Register your models here.
admin.site.register(PropertyGroup)
admin.site.register(PropertyItem)
admin.site.register(OwnerAddress)
admin.site.register(FoundLocation)
admin.site.register(SealNumber)
admin.site.register(StoredLocation)
admin.site.register(FoundAddress)
admin.site.register(Owner)
admin.site.register(PropertyItemImage)
