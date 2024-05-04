import django_filters
from django import forms

from django.contrib.auth.models import User

from moobile.models import Product, Category, Tag

class ProductFilter(django_filters.FilterSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    date_range = django_filters.DateRangeFilter(
        field_name='date',
        empty_label='Выберите вариант',
        widget=forms.Select(attrs={
            'class': 'mb-4 border border-current rounded-none p-2 form-select border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500'
        })
    )

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'mb-2 border border-current rounded-none p-2 form-checkbox border-gray-300'
        })
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'mb-4 border border-current rounded-none p-2 form-select border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500'
        })
    )

    author = django_filters.ModelChoiceFilter(queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'mb-4 border border-current rounded-none p-2 form-select border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Min Price',
        widget=forms.NumberInput(attrs={
            'class': 'mb-4 border border-current rounded-none p-2 form-input border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': 'Min Price'
        })
    )
    
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Max Price',
        widget=forms.NumberInput(attrs={
            'class': 'mb-4 border border-current rounded-none p-2 form-input border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': 'Max Price'
        })
    )

    class Meta:
        model = Product
        fields = ('tags', 'category', 'author','min_price', 'max_price')
