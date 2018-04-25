from django.shortcuts import render
from wordlist.forms import *
from wordlist.models import *
# Create your views here.


def list(request):
	wordList = Word.objects.all()
	return render(request, 'list.html',{'wordList':wordList})

def input(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()

	return render(request, 'input.html', {'form':form})

def view(request, num='1'):
	word = Word.objects.get(id=num)
	return render(request, 'view.html', {'word':word})
