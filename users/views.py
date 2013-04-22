from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
# Create your views here.

def nuevo_usuario(request):
	if request.method == 'POST':
			# formulario enviado
			user_form = UserCreationForm(request.POST, )
			
			if user_form.is_valid():
				# formulario validado correctamente
				user_form.save()
				return render_to_response('guardado.html')

	else:
			# formulario inicial
			user_form = UserCreationForm()
			

	return render_to_response('nuevo.html', { 'formulario': user_form}, context_instance=RequestContext(request))

