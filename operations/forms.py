from django.forms import forms
from operations.models import Treatment

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit

class TreatmentForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Treatment
        fields = ['patient', 'doctor', 'date', 'symptoms', 'diagnosis', 'doctors_comments']

        labels = {
            'doctors_comments': "Doctor's Comments"
            }

    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'patient',
            'doctor',
            'date',
            MultiWidgetField(
                'date',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            'symptoms',
            'diagnosis',
            'doctors_comments',
        )


    def clean(self):
        cleaned_data = super(TreatmentForm, self).clean()
        return cleaned_data