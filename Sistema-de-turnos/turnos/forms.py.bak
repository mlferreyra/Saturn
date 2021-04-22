from django import forms
from turnos.models import Turno,ObraSocial,Medico,Especialidad
from django.core.exceptions import ValidationError

class MedicoModelChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        key = self.to_field_name or 'pk'
        value = Medico.objects.filter(**{key: value})
        if not value.exists():
            raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
        else:
            value= value.first()
        print(value)
        return value

class TurnoForm(forms.ModelForm):
    medico = MedicoModelChoiceField(queryset = Medico.objects.none(), widget=forms.Select(attrs={'class': 'form-control turn'}))
    class Meta:
        model = Turno
        

        fields = [
            'fecha_turno',
            'especialidad', 
            'medico',
            'obrasocial',           
            'nombre',
            'dni',
            'edad',
            'telefono',
            'mail',            
            'sexo',            
        ]
        label = {
            'fecha_turno':'fecha_turno',
            'especialidad':'Especialidad',            
            'medico':'Medico',      
            'obrasocial':'Obra Social',           
            'nombre':'Nombre',
            'dni':'DNI',
            'edad':'Edad',
            'telefono':'Teléfono',
            'mail':'Email',
            'sexo':'Sexo',            
        }
        widgets = {
            'fecha_turno':forms.DateInput(attrs={'class': 'form-control turn', 'type':'date'}),    
            'fecha_registro':forms.DateInput(attrs={'class':'form-control turn'}),
            'especialidad':forms.Select(attrs={'class':'form-control turn'}),
            'medico':forms.Select(attrs={'class':'form-control turn'}),
            'obrasocial':forms.Select(attrs={'class':'form-control turn'}),      
            'nombre':forms.TextInput(attrs={'class':'form-control turn'}), 
            'dni':forms.TextInput(attrs={'class':'form-control turn'}),
            'edad':forms.NumberInput(attrs={'class':'form-control turn datepicker'}),
            'telefono':forms.TextInput(attrs={'class':'form-control turn'}),       
            'mail':forms.TextInput(attrs={'class':'form-control turn'}),      
            'sexo':forms.Select(attrs={'class':'form-control turn'}),        
        }