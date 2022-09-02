from django import forms

class BocaFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    goles=forms.IntegerField()
    

class RiverFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    goles=forms.IntegerField()
  

class SanlorenzoFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    goles=forms.IntegerField()


