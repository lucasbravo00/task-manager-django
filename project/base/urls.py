from django.urls import path
from .views import TaskList, TaskCreate, TaskEdit, TaskDelete, LoginViewCustom, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Home route showing the list of tasks
    path('', TaskList.as_view(), name='tasks'),

    # Login and registration routes
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

    # Logout view that redirects to login page after logging out
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Create, edit, and delete task views
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('edit-task/<int:pk>', TaskEdit.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
]
