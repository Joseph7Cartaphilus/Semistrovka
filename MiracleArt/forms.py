from django import forms

from .models import Pin


class EditForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        self.instance.user = self.initial['user']
        return super(EditForm, self).save(*args, **kwargs)

    class Meta:
        model = Pin
        fields = ('title', 'text', 'category', 'img')

    def clean(self):
        self.cleaned_data['title'] = self.cleaned_data['title'].upper()
        return self.cleaned_data
