from django.urls import path
from .views import indexPageView, campingPageView, hikingPageView, climbingPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("camping/<trip_name>", campingPageView, name = "camping"),
    path("hiking/", hikingPageView, name = "hiking"),
    path("climbing/", climbingPageView, name = "climbing"),
]
