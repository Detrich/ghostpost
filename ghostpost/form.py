from django import forms

ROASTORBOAST = (
    (False, 'Roast'),
    (True, 'Boast')
)
class addRorB(forms.Form):
    roastorboast = forms.ChoiceField(choices=ROASTORBOAST, widget=forms.RadioSelect(), help_text='Roast or Boast:')
    content = forms.CharField(max_length=280,widget=forms.Textarea, help_text='Write a Roast or a Boast here (max 280 char) :')