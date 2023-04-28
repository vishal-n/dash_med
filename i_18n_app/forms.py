from django import forms
import json

class JSONWidget(forms.Widget):
    def decompress(self, value):
        if value:
            return json.loads(value)
        return ['', '']

    def format_output(self, rendered_widgets):
        return '<br>'.join(rendered_widgets)

class JSONFormField(forms.CharField):
    widget = JSONWidget

    def clean(self, value):
        if value is None:
            value = ''

        try:
            value_dict = json.loads(value)
        except ValueError:
            raise forms.ValidationError("Invalid JSON data")

        cleaned_data = {}
        for key, val in value_dict.items():
            if not val:
                continue
            cleaned_data[key] = val

        return json.dumps(cleaned_data)