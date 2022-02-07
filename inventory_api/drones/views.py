from rest_framework import generics
from .models import Drones
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponse, HttpResponseRedirect
 


class PostList(generics.ListCreateAPIView):
    queryset = Drones.objects.all()
    serializer_class= PostSerializer

     # Post only possible when authenticated
     # without authentication read only
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Redirect to main API page after post was made
    def create(self, request, *args, **kwargs):
        response = super(PostList, self).create(request, *args, **kwargs)
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        return HttpResponseRedirect(redirect_to='')

"""    def perform_create(self, serializer):
        serializer.partial = True
        serializer.save(created_by=self.request.user)"""


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Drones.objects.all()
	serializer_class = PostSerializer

