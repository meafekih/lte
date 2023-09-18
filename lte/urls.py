from django.urls import path
from .views import (index, login, forgot_password,
    register, faq, contact_us, sales_list, profile,
    followers, pricing, )

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('register/', register, name='register'),
    path('faq/', faq, name='faq'),
    path('contact_us/', contact_us, name='contact_us'),
    path('sales_list/', sales_list, name='sales_list'),
    path('profile/', profile, name='profile'),
    path('followers/', followers, name='followers'),
    path('pricing/', pricing, name='pricing'),

    
]
