from cProfile import label
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NewPostForm(forms.Form):
    title = forms.CharField(label='Post title')
    content = forms.CharField(label='Your post body')
    image = forms.ImageField(required=False)
    pub_date = forms.DateTimeField( 
        initial=datetime.datetime.now(),
        disabled=True
    )

class NewCommentForm(forms.Form):
    content = forms.CharField()