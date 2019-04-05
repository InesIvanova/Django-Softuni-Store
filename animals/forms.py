from django import forms
from .models import Animal
from django.core.validators import RegexValidator, URLValidator, MinValueValidator


class AnimalForm(forms.ModelForm):

    choices = list(Animal.KIND_CHOICES)

    name = forms.CharField(required=True,
                           validators=[RegexValidator(r'^[A-Z][a-z]+$', message="Animal's name must start with capital latain letter, followed by latain small letters.")],
                           widget= forms.TextInput(
                               attrs= {
                                   'class': 'form-control'
                               }
                           ))
    age = forms.IntegerField(required=True,
                             min_value=0,
                             validators=[RegexValidator(r'^\d+$', message='The age must be positive number ot 0')],
                             widget=forms.NumberInput(
                                 attrs = {
                                     'class': 'form-control'
                                 }
                             ))
    breed = forms.CharField(required=True,
                            validators=[RegexValidator(r'^[A-Z][a-z]+$',
                                                       message="Animal's breed must start with capital latain letter, followed by latain small letters.")],
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }
                            )
                            )
    image_url = forms.URLField(required=True,
                               widget=forms.TextInput(
                                   attrs= {
                                       'class': 'form-control'
                                   }
                               ))
    kind = forms.ChoiceField(choices=choices,
                                widget=forms.Select(
                                    attrs= {
                                        'class': 'form-control'
                                    }
                                )
                             )

    class Meta:
        model = Animal
        fields = ('name', 'age', 'breed', 'description', 'image_url', 'kind')
