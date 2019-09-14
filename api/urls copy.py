from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

#from .views import ListEventsView,ListNewsView,CustomRegisterView


urlpatterns = [
   # path('events/', ListEventsView.as_view(), name="events-all"),
   # path('news/', ListNewsView.as_view(), name="news-all"),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
   # path('auth/', CustomRegisterView.as_view(), name="auth-all"),

]