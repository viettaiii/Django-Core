from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField

class BookFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'
        self.form_class = 'row g-3 align-items-center'  # Bootstrap row với spacing
        self.layout = Layout(
            Row(
                Column(FloatingField('title'), css_class='col-md-3'),
                Column(FloatingField('author'), css_class='col-md-2'),
                Column(FloatingField('genre'), css_class='col-md-2'),
                css_class='align-items-center'
            ),
            Submit('submit', 'Apply Filters', css_class='btn btn-primary col-md-2 mt-3')
        )