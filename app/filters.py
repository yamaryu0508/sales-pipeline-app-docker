import django_filters
from django.db import models

from .models import Item


class OrderingFilter(django_filters.filters.OrderingFilter):
    descending_fmt = '%s (Descending order)'


class ItemFilterSet(django_filters.FilterSet):

    # Sort order on search form
    order_by = OrderingFilter(
        initial='Created datetime',
        fields=(
            ('created_at', 'created_at'),
            ('updated_at', 'updated_at'),
        ),
        field_labels={
            'created_at': 'Created datetime',
            'updated_at': 'Updated datetime',
        },
        label='Sort order'
    )

    class Meta:
        model = Item
        exclude = ['created_at', 'updated_by', 'updated_at', ]
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
