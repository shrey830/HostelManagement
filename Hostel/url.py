from django.urls import path
from Hostel import views

urlpatterns = [
    path('',views.register_page,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('index/',views.index,name='index'),
    path('booking/',views.booking,name='booking'),
    # path('selectroom/',views.selectroom,name='selectroom'),
    path('confirmbooking/',views.confirmbooking,name='confirmbooking'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('facilities/',views.facilities,name='facilities'),
    path("facilities1/<str:room1>/", views.facilities1, name="facilities1"),
    path('contact/',views.contact_view,name='contact')
]

