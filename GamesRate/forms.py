from django import forms

class JuegoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)
    estrellas = forms.IntegerField()
    opinion = forms.CharField(max_length=200)