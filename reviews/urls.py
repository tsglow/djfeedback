from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name="index" ),       
    path('list', views.ReviewListView.as_view(), name="list"),
    path('list/favorite',views.AddFavorite.as_view()),
    path('list/<int:pk>', views.DetailView.as_view(), name="detail"),     
    path('thank', views.ThankView.as_view(), name="thank"),
    
]