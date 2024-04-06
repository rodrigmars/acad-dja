from django.contrib import admin
from django.urls import path
from informativos.views import home
from alunos.views import aluno_lista

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="informativos_home"),
    path("alunos/", aluno_lista, name="aluno_lista"),
]
