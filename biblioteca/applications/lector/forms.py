from django import forms 


from .models import Prestamo


class PrestamoForm (forms.ModelForm):

    success_url = '.'
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )


