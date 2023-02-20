from django_filters import rest_framework as dj_filters
from .models import TodoList


class ToDoListFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    title = dj_filters.CharFilter(field_name="title", lookup_expr="icontains")
    is__done = dj_filters.BooleanFilter(field_name="is_done", lookup_expr="icontains")

    order_by_field = "ordering"

    class Meta:
        model = TodoList
        fields = [
            "title",
            "is_done",
        ]