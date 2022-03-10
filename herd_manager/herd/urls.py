
from django.urls import path

from .views import herd_list_view, animal_add_view, animal_update_view,\
    animal_delete_view, test, table_view, login_page, register_page, logout_user



urlpatterns = [
    path('', herd_list_view, name='animal-view'),
    path('add/', animal_add_view),
    path('update/<int:pk>', animal_update_view, name="update"),
    path('delete/<int:pk>', animal_delete_view, name="delete"),
    path('test/<int:pk>', test, name="test"),
    path('table/', table_view, name="table_view"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', logout_user, name="logout")

]
