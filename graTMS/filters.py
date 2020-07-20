import django_filters
from graTMS.models import Complaint


class ComplaintFilter(django_filters.FilterSet):
    class Meta:
        model = Complaint
        fields = ('user', 'office')
