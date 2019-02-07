from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('btc-trade/', views.btc_trade, name='btc_trade'),
    path('posts/<int:question_id>/', views.detail, name='detail')
]