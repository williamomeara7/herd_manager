
from django import forms

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
    type = forms.ChoiceField(choices=CHOICES_TYPE)
    letter_grade = forms.ChoiceField(choices=CHOICES_LETTER)
    number_grade = forms.ChoiceField(choices=CHOICES_NUMBER)

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


