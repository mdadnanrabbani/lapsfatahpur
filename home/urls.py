
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('contactus', views.contactus, name="Contact Us"),
    path('about', views.about, name="About Us"),
    path('academics', views.academics, name="Academics"),
    path('admissions', views.admissions, name="Academics"),
    path('campuslife', views.campuslife, name="Academics"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('writenotice', views.writenotice, name="Write Notice"),
    path('circular', views.circulars, name="View Circular"),
    path("circulars/api/", views.circulars_api, name="circulars_api"),
    path('notice/<int:notice_id>/', views.notice_detail, name="notice_detail"),
    path("notice/<int:pk>/download/", views.notice_download, name="notice_download"),

]


