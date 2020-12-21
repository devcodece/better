from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    #metodo __init__ ejecuta toda clase de python
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Password'