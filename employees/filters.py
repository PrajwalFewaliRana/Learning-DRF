import django_filters
from .models import Employee

#same as serializer
class EmployeeFilter(django_filters.FilterSet):
    #iexact also accept case insensitive letters
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    
    
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    
    
    # id = django_filters.RangeFilter(field_name='id') #only accepts int value
    
    #now this will accept range of char value
    id_min= django_filters.CharFilter(method='filter_by_id_range',label='From EMP ID')
    id_max= django_filters.CharFilter(method='filter_by_id_range',label='To EMP ID')
    
    
    
    class Meta:
        model = Employee
        fields = ['designation','emp_name','id_min','id_max']
    
    def filter_by_id_range(self,queryset,name,value):
        if name =='id_min':
            return queryset.filter(emp_id__gte=value) #value contains minimum range ie starting range
        elif name =='id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset