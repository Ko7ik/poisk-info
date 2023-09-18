from django_filters import rest_framework as filters
from backend_api.models import FoundData


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TaskFilter(filters.FilterSet):
    task = CharFilterInFilter(field_name='id_task', lookup_expr='in')

    class Meta:
        model = FoundData
        fields = ['id_task']
