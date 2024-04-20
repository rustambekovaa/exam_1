from django import forms 

from moobile.models import Category, Tag,Product

class ProductForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите заголовок'}))
    price = forms.CharField(label='Цена', widget=forms.NumberInput(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите цену'}))
    image = forms.ImageField(label='Изображение', widget=forms.FileInput(
        attrs={'accept': 'image/*', 'class': 'form-control',}))
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Контент'}))
    is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput())
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())



# class ProductForm(forms.ModelForm):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['category'].empty_label = 'Выберите категорию'


#     class Meta:
#         model = Product
#         fields = ['title','price','image','is_published','content','category','tags']

#         widgets = {
#                 'title': forms.TextInput(attrs={'class':'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите заголовок'}),
#                 'price': forms.NumberInput(attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-100', 'placeholder': 'Цена'}),
#                 'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
#                 'content': forms.Textarea(attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Контент'}),
#                 'category': forms.Select(attrs={'class': 'form-select'}),
#                 'tags': forms.CheckboxSelectMultiple()
#             }
    



class UpdateForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите заголовок'}))
    price = forms.CharField(label='Цена', widget=forms.NumberInput(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите цену'}))
    image = forms.ImageField(required=False,label='Изображение', widget=forms.FileInput(
        attrs={'accept': 'image/*', 'class': 'form-control',}))
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Контент'}))
    is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput())
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())

