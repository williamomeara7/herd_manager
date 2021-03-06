from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Animal
















CHOICES_TYPE = (
    ("Cow", "Cow"), ("Young Bull", "Young Bull"), ("Steer", "Steer"), ("Bull", "Bull"), ("Heifer", "Heifer")
)

CHOICES_LETTER = (
    ("E+", "E+"), ("E=", "E="), ("E-", "E-"), ("U+", "U+"), ("U=", "U="), ("U-", "U-"), ("R+", "R+"), ("R=", "R="),
    ("R-", "R-"), ("O+", "O+"), ("O=", "O+"), ("O-", "O-"), ("P+", "P+"), ("P=", "P="), ("P-", "P-"))

CHOICES_NUMBER = (
    ("1-", "1-"), ("1=", "1="), ("1+", "1+"), ("2-", "2-"), ("2=", "2="), ("2+", "2+"), ("3-", "3-"), ("3=", "3="),
    ("3+", "3+"), ("4-", "4-"), ("4=", "4="), ("4+", "4+"), ("5-", "5-"), ("5=", "5="), ("5+", "5+")
)
class AnimalForm(forms.ModelForm):
    type = forms.ChoiceField(choices=CHOICES_TYPE, widget=forms.RadioSelect())
    letter_grade = forms.ChoiceField(choices=CHOICES_LETTER, widget=forms.RadioSelect())
    number_grade = forms.ChoiceField(choices=CHOICES_NUMBER, widget=forms.RadioSelect())


    class Meta:
        model = Animal

        fields = [
            'type',
            # 'description',
            'letter_grade',
            'number_grade',
            'price',
            'weight'
        ]




class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

