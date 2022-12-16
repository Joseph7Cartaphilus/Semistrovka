from django import forms

from .models import Pin


class EditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=forms.TextInput())
    img = forms.ImageField(widget=forms.FileInput(), required=False)
    category = forms.HiddenInput()

    def save(self, *args, **kwargs):
        self.instance.user = self.initial['user']
        return super(EditForm, self).save(*args, **kwargs)

    class Meta:
        model = Pin
        fields = ('title', 'text', 'category', 'img')
