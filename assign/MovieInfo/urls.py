
from django.urls import path
from MovieInfo import views

urlpatterns=[
    path('',views.home ,name="home"),
    path('api/',views.BookListInfo.as_view(),name="booklist"),
    path('?<int:q>/', views.BookDetailView.as_view(),name="book-detail"),
    
]