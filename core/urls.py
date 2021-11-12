from django.urls import path
from .views import Duvidas, index, cliente_novo, landingPage, lojaVirtual, siteInstitucional, socialMedia, sobreNos, Portifolio, Contato, Orcamento

urlpatterns = [
    path('', index, name='index'),
    path('cliente_novo/', cliente_novo, name='cliente_novo'),
    # serviços
    path('landing_page', landingPage, name='landing_page'),
    path('site_institucional', siteInstitucional, name='site_institucional'),
    path('loja_virtual', lojaVirtual, name='loja_virtual'),
    path('social_media', socialMedia, name='social_media'),
    # Sobre nós
    path('sobre_nos', sobreNos, name='sobre_nos'),
    # Portifolio
    path('portifolio', Portifolio, name='portifolio'),
    # duvidas
    path('duvidas', Duvidas, name='duvidas'),
    # contato
    path('contato', Contato, name='contato'),
    # orcamento
    path('orcamento', Orcamento, name='orcamento'),
]
