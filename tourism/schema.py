import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import attractions

#Create a GraphQL type for the actor model
class AttractionType(DjangoObjectType):
    class Meta:
        model = attractions


#Create a query type
class Query(ObjectType):
    attraction = graphene.Field(AttractionType, id=graphene.Int())
    attraction_list = graphene.List(AttractionType)

    def resolve_attraction(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return attractions.objects.get(pk=id)

        return None

    def resolve_attraction_list(self, info, **kwargs):
        return attractions.objects.all()

schema=graphene.Schema(query=Query,mutation=None)
