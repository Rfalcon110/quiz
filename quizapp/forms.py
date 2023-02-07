
from django.forms import ModelForm
from .models import *

class ScqForm(ModelForm):
    class Meta:
        model=Scq
        fields="__all__"
class addquizform(ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'       
class McqForm(ModelForm):
    class Meta:
        model=Mcq
        fields='__all__'
class BooleanForm(ModelForm):
    class Meta:
        model=booleanques
        fields='__all__'
class IntForm(ModelForm):
    class Meta:
        model=intques
        fields='__all__'
