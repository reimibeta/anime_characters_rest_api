# from django.shortcuts import render

# from rest_framework import viewsets, status, filters
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.authtoken.serializers import AuthTokenSerializer

# from .serializers import UserProfileSerializer
# from .models import UserProfile
# from .permissions import UpdateOwnProfile

# class LoginViewSet(viewsets.ViewSet):
#     """ Checks email and password and returns an auth token. """

#     serializer_class = AuthTokenSerializer

#     def create(self, request):
#         """ Use the ObtainAuthToken APIView to validate and create a token. """
#         return ObtainAuthToken().post(request)

# class UserProfileViewSet(viewsets.ModelViewSet):
#     """ Handles creating, creating and updating profiles. """

#     serializer_class = UserProfileSerializer
#     queryset = UserProfile.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (UpdateOwnProfile,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name', 'email', )

# # class UserProfileFeedViewSet(viewsets.ModelViewSet):
# #     """ Handles creating, reading and updating profile feed items. """

# #     authentication_classes = (TokenAuthentication,) 
# #     serializer_class = 