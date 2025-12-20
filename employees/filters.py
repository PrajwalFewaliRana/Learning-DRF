import django_filters
from .models import Employee

#same as serializer
class EmployeeFilter(django_filters.FilterSet):
    #iexact also accept case insensitive letters
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    class Meta:
        model = Employee
        fields = ['designation']