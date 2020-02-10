from django import forms
from . models import PropertyItemImage, PropertyGroup, PropertyItem, OwnerAddress, FoundAddress, FoundLocation, SealNumber, StoredLocation, Owner

class PropertyItemImageForm(forms.ModelForm):
    class Meta:
        model = PropertyItemImage
        fields = [
            'image',
        ]

class PropertyGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyGroupForm, self).__init__(*args, **kwargs)
        self.fields['group_ID'].label = 'External reference'
        self.fields['group_ID'].widget.attrs.update({'placeholder': 'Log / Crime reference etc...'})
        self.fields['subject_surname'].widget.attrs.update({'placeholder': 'Add surname if known'})
        self.fields['group_ID'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = PropertyGroup
        fields = [
            'group_ID',
            'subject_surname'
        ]

class PropertyItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyItemForm, self).__init__(*args, **kwargs)
        self.fields['sub_location'].label = 'Sub location'
        self.fields['sub_location'].widget.attrs.update({'placeholder': 'Bedroom / Car & Registration / Kitchen etc...'})
        self.fields['description'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = PropertyItem
        fields = [
            'description',
            'exhibit_reference',
            'seized_by',
            'seized_time',
            'seized_date',
            'sub_location',
            'notes',
        ]

class FoundAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoundAddressForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs.update({'placeholder': 'Add notes here'})
        self.fields['flat_number'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = FoundAddress
        fields = [
            'flat_number',
            'house_number',
            'house_name',
            'road_name',
            'town',
            'postcode',
            'notes',
        ]

class FoundLocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoundLocationForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs.update({'placeholder': 'Add notes here'})
        self.fields['word_one'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = FoundLocation
        fields = [
            'word_one',
            'word_two',
            'word_three',
            'notes',
        ]

class SealNumberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SealNumberForm, self).__init__(*args, **kwargs)
        #override fields HttpResponseRedirect
    class Meta:
        model = SealNumber
        fields = [
            'seal_reference',
        ]

class OwnerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs.update({'placeholder': 'Add notes here'})
        self.fields['company'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = Owner
        fields = [
            "company",
            "first_name",
            "last_name",
            "date_of_birth",
            "mobile",
            "telephone",
            "email",
            "notes",
        ]

class OwnerAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnerAddressForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs.update({'placeholder': 'Add notes here'})
        self.fields['flat_number'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model = OwnerAddress
        fields = [
            'flat_number',
            'house_number',
            'house_name',
            'road_name',
            'town',
            'postcode',
            'notes',
        ]
