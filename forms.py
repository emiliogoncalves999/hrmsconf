from django import forms
from custom.models import RequestSet
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from purchase_request.models import *






class RequestSetForm(forms.ModelForm):

    class Meta:
        model = RequestSet
        fields = ['group']

    def __init__(self, *args, **kwargs):
        super(RequestSetForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('group', css_class='col-md-12'),

            ),


            Div(
                    # Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Add ba timeline', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['group'].widget.attrs['class'] = 'form-control'

