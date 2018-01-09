from django.urls import path
from . import views
urlpatterns=[
    path('',views.PortflioListView.as_view(),name='portfolio-list'),
    path('<slug:slug>/',views.PortfolioDetailView.as_view(),name='portfolio-detail'),
]