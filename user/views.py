from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from . forms import LoginForm

# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    #decorador para proteccion
    @method_decorator(csrf_protect)
    #No guardar en cache
    @method_decorator(never_cache)

    #reescribiendo  el metodo dispath
    def dispatch(self, request, *args, **kwargs):
        #verificar si el usuario esta logueado
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_succes_url())
        #si no esta logueado redirigir a login.html
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    
    #redifinir el metodo form_valid
    def form_valid(self, form):
        #Indicarle a Django que inicie una sesion despues de loguearse
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')