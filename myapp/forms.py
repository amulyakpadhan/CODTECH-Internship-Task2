from django import forms

ASPECT_RATIO_CHOICES = [
        ('1:1', '1:1'),
        ('4:3', '4:3'),
        ('16:9', '16:9')
    ]


class ImageGenerationForm(forms.Form):
    prompt = forms.CharField(
        label='Text',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a text description for the image...'
        })
    )
    aspect_ratio = forms.ChoiceField(
        label='Aspect Ratio',
        choices=ASPECT_RATIO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )