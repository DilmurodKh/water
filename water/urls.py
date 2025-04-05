from django.urls import path
from .views import WaterlsitView, WaterCreatView, WaterDeleteView,WaterDetialView,WaterUpDateView

urlpatterns = [
    path('waters',WaterlsitView.as_view()),
    path('create',WaterCreatView.as_view(),),
    path('<int:pk>/',WaterDetialView.as_view()),
    path('<int:pk>/update/',WaterUpDateView.as_view()),
    path('<int:pk>/delete/',WaterDeleteView.as_view()),
]

