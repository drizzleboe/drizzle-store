import django_filters
from .models import *

class productFilter(django_filters.FilterSet):
    title_name = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='')
    #class Meta:
    #    model = product
    #    fields = ['title','price']