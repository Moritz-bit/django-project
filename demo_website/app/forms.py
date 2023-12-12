from django import forms

attribute = {"class":"custom-control-input"}
class CheckinForm(forms.Form):
    squatcheckbox = forms.BooleanField(
        widget=forms.CheckboxInput(attrs=attribute),
        required=False,
        initial=False #switchvalues[0]
        )
    benchcheckbox = forms.BooleanField(
        widget=forms.CheckboxInput(attrs=attribute),
        required=False,
        initial=False #switchvalues[1]
        )
    deadliftcheckbox = forms.BooleanField(
        widget=forms.CheckboxInput(attrs=attribute),
        required=False,
        initial=False #switchvalues[2]
        )
    submit_msg = "hidden"