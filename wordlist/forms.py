from django.forms import ModelForm
from wordlist.models import *

class Form(ModelForm):
	class Meta:
		model = Word
		fields=['word','meaning']