"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno.views import *

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('cadastrar/alunos/', cadastrar_aluno),
    path('listar/alunos/', lista_alunos),
    path('aluno/<int:id>', detalhes_aluno),
    path('atualizar/aluno/<int:id>', atualizar_aluno),
    path('deletar/aluno/<int:id>', deletar_aluno)
]
