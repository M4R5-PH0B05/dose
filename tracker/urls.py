from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("view_med/<int:med_id>", views.view_med, name="view_med"),
    path("add_med", views.add_med,name="add_med"),
    path("delete_med/<int:med_id>", views.delete_med,name="delete_med"),
    path("edit_med/<int:med_id>",views.edit_med,name="edit_med"),
    path("mark_taken/<int:med_id>",views.mark_taken,name="mark_taken"),
    path('register/', views.register, name="register")
]
