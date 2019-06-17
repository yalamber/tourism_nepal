from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
