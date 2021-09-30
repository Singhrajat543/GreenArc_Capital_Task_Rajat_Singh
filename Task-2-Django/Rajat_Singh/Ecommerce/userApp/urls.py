from django import forms
from django.urls import path
from userApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm 
from .forms import MyPasswordChangeForm 
from .forms import MyPasswordResetForm 
from .forms import MyForgotenPassForm

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),  
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('Removecart/', views.remove_cart, name='Removecart'),



    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.Laptop, name='laptop'),
    path('laptop/<slug:data>', views.Laptop, name='laptopdata'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),  
    path('UploadProduct/', views.Upload_Product , name='UploadProduct'),   
 




    path('accounts/login/', auth_views.LoginView.as_view
    (template_name='app/login.html', authentication_form=LoginForm ), name='accounts/login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts/login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
     form_class=MyPasswordChangeForm , success_url='/PasswordChangeDone/'), name='passwordchange'),

     path('PasswordChangeDone/', auth_views.PasswordChangeView.as_view(template_name='app/PasswordChangeDone.html'),
      name='PasswordChangeDone'),

    path('password-reset/', auth_views.PasswordResetView.
    as_view(template_name='app/common/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),  
    
    path('password_reset_done/done/', auth_views.PasswordResetDoneView.
    as_view(template_name='app/common/password_reset_done.html'),name='password_reset_done'),  

    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.
    as_view(template_name='app/common/password_reset_confirm.html',form_class=MyForgotenPassForm),name='password_reset_confirm'),  

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.
    as_view(template_name='app/common/password_reset_complete.html'),name='password_reset_complete'),  


    
    path('registration/', views.CostomerRegistrationView.as_view(), name="customerregistration")
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
 