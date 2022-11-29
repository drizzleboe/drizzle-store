from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('index/<slug:slug_field>', views.details, name="details"),
    path('index/order/', views.placed_order, name='placed_order'),
    path('register', views.register, name="register"),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('userlist', views.userlist, name='userlist'),
    path('myaccount/<int:user_id>', views.myaccount, name="myaccount"),
    path('settings', views.settings, name='settings'),
    path('about_us', views.about, name='about'),
    path('aftersub', views.tester, name="test"),
    path('faqs', views.faq, name='faqs'),
    path('subscription', views.subs, name='subscription'),
    path('success', views.success, name='success'),
    path('products', views.products, name='products'),
    path('cart', views.cart, name = 'cart'),
    path('contact_us', views.contact, name='contact_page'),

    ######################################################
    ######################################################
    
    path('to_admins/622/admins/admin/login', views.admin_login, name='admins_login'),
]