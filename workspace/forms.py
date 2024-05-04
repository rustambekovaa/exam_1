from django import forms 
from moobile.models import  Product
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'image',
            'content',
            'is_published',
            'category',
            'tags',
            
        ]

        # labels = {
        #     'name': 'Custom name label'
        # }

        widgets = {
                'title': forms.TextInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите заголовок'}),
                'price': forms.NumberInput(attrs={'class': 'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-100', 'placeholder': 'Цена'}),
                'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
                'content': forms.Textarea(attrs={'class': ' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Контент'}),
                'category': forms.Select(attrs={'class': ' mb-4 form-select'}),
                'tags': forms.CheckboxSelectMultiple()
            }
    


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'mb-4 border border-current rounded-none p-2 form-input border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'mb-4 border border-current rounded-none p-2 form-input border-gray-300 block w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Пароль'}))
    



class RegisterForm(BaseUserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Придумайте пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
        attrs={'class':' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Подтвердите пароль'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Придумайте имя пользователя'}),
            'email': forms.EmailInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите эл. почту'}),
        }




class ChangeProfileForm(forms.ModelForm):

    # email = forms.EmailField(label='Эл. почта', required=True,
    #                          widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите эл. почту'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class':' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500','placeholder': 'Введите фамилию'}),
            'username': forms.TextInput(attrs={'class': 'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'class':'mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Введите эл. почту'})
        }

    



class ChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user: User = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class':' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500','placeholder': 'Текущий пароль'}))
    new_password = forms.CharField(label='Новый пароль',
                                   widget=forms.PasswordInput(attrs={'class':' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500','placeholder': 'Введите новый пароль'}),
                                   validators=[validate_password])
    confirm_password = forms.CharField(label='Подтвердите пароль',
                                       widget=forms.PasswordInput(attrs={'class':' mb-4 border border-current rounded-none p-2 w-full focus:ring-indigo-500 focus:border-indigo-500','placeholder': 'Подтвердите'}))

    def clean(self):
        data = self.cleaned_data

        password = data.get('password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        errors = {}

        if not self.user.check_password(password):
            errors['password'] = ['The password is incorrect.']

        if new_password != confirm_password:
            errors['confirm_password'] = ['The passwords do not match.']

        if len(errors) > 0:
            raise forms.ValidationError(errors)

        return data