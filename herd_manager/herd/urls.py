
from django.urls import path

from .views import herd_list_view, animal_add_view, animal_update_view, animal_delete_view


urlpatterns = [
    path('', herd_list_view, name='animal-view'),
    path('add/', animal_add_view),
    path('update/<int:pk>', animal_update_view, name="update"),
    path('delete/<int:pk>', animal_delete_view, name="delete")

]
