from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CurrentUserView, NoteListCreateView, TodoListCreateView

urlpatterns = [
    # JWT login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Current logged-in user
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('notes/', NoteListCreateView.as_view(), name='notes'),
    path('todos/', TodoListCreateView.as_view(), name='todos'),

]
