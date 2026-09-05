from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),

    path('signup/', views.signup_page, name='signup'),

    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('notifications/', views.notifications, name='notifications'),
path('add-staff/', views.add_staff, name='add_staff'),
    path('products/', views.manage_products, name='manage_products'),
    path('product-status/', views.product_status, name='product_status'),
    path('add-product/', views.add_product, name='add_product'),
    

    path('staff-management/', views.staff_management, name='staff_management'),
    path('activity-log/', views.activity_log, name='activity_log'),
    path('account/', views.account, name='account'),

    path('logout/', views.logout_page, name='logout'),
]