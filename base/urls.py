from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from .forms import LoginForm

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='login.html'), name="login"),
]
'''
inja gharare pashmat berize. ghablesh boro va doc forms.py ro check kon.
bbin kolan varay login lazem nist view benevisi va be jash miyay module
'from django.contrib.auth import views as auth_views'
ro seda mozani. dar asl ye views.py dare khodesh ke tosh ye view hast be 
esm LogView ke az type generic view ha ham hast va on ro add midi.
badesh form login ro az forms.py seda mikoni va badesh be generic view 
login in arguemnt ro midi:
'authentication_form=LoginForm' 
ke LoginForm ham esm fomrmete.
'''