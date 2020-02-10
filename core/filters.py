import django_filters

class PropertyItemFilter(django_filters.FilterSet):
    class Meta:
        model = PropertyItem
        fields = [
            'description',
            'seized_by',
            'exhibit_reference',
            'seized_time',
            'seized_date',
            'sub_location',
            'notes',
        ]
