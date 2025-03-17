from django.urls import path
from django.contrib.auth import views as auth_views
from .views import frontpage, create_note, delete_task, note_detail, signup, logout_view

urlpatterns = [
    path("", frontpage, name="frontpage"),  
    path("create/", create_note, name="create_note"),  
    path("delete/<int:note_id>/", delete_task, name="delete_task"),
    path('note/<int:note_id>/', note_detail, name='note_detail'),  # 👈 Add this
    path("signup/", signup, name="signup"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", logout_view, name="logout"),  # ✅ Use the correct logout view
    path("note/<int:note_id>/", note_detail, name="note-detail"),  # ✅ Correct URL
    path("create/", create_note, name="create-note"),
    path("delete/<int:note_id>/", delete_task, name="delete_task"),
]
