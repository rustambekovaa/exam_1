# from django import forms
# from .models import *

# class AddPostForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)