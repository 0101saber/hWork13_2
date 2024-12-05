from django.forms import ModelForm, CharField, DateField, TextInput, SelectDateWidget, SelectMultiple
from .models import Author, Quote


class AuthorForm(ModelForm):
    born_date = DateField(
        widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(1985, 2015)),
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = Author
        fields = ['description', 'fullname', 'born_date', 'born_location']
        widgets = {
            'description': TextInput(attrs={"class": "form-control", "id": "description"}),
        }

    def clean_born_date(self):
        born_date = self.cleaned_data['born_date']
        return born_date.strftime('%B %d, %Y')


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
        widgets = {
            'tags': SelectMultiple(attrs={"class": "form-control"}),
        }
