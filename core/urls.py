from django.urls import path
from .views import index, cliente_novo, email


urlpatterns = [
    path('', index, name='index'),
    path('cliente_novo/', cliente_novo, name='cliente_novo'),
    path('email/', email, name='email'),
]
