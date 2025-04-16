from . import views
from django.urls import path

app_name = 'examapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('about us',views.about, name='about'),
    path('shop/<str:foo>',views.shop, name='shop'),
    path('index',views.index, name='index'),
    path('add_service',views.add_service, name='add_service'),
    path('remove_service<int:service_id>',views.remove_service, name='remove_service'),
    path('update_service<int:service_id>',views.update_service, name='update_service'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register_user, name='register'),
    path('service/<int:pk>',views.service, name='service'),
    # path('category/<str:foo>',views.category, name='category'),
]
