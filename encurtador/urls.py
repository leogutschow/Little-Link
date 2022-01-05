from django.urls import path
from .views import IndexView, redirect_view, link_encurtado

app_name = 'encurtador'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('encurtado', link_encurtado, name='link_encurtado'),
    path('<str:link_curto>', redirect_view, name='redirect')
]
