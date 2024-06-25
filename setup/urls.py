from django.contrib import admin
from django.urls import path
from todos.views import TodoCompleteView,TodosListVieW,TodoCreateView, TodoDeleteView,TodoUpdateVieW

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",TodosListVieW.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateVieW.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
