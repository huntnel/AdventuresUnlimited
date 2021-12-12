from django.urls import path
from .views import indexPageView, storeHikePageView, updateCampPageView, updateHikePageView, storeCampPageView, campingPageView
from .views import hikingPageView, createHikePageView, createCampPageView, updateHikePageView, updateCampPageView
from .views import deleteCampPageView, deleteHikePageView, aboutPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about/", aboutPageView, name="about"),
    path("camping/", campingPageView, name = "camping"),
    path("hiking/", hikingPageView, name = "hiking"),
    path("createhike/", createHikePageView, name = "createhike"),
    path("createcamp/", createCampPageView, name = "createcamp"),
    path("updatehike/", updateHikePageView, name = "updatehike"),
    path("updatecamp/", updateHikePageView, name = "updatehike"),
    path("deletehike/", deleteHikePageView, name = "deletehike"),
    path("deletehike/", deleteHikePageView, name = "deletehike"),
    path("storehike/", storeHikePageView, name = "storehike"),
    path("storecamp/", storeCampPageView, name = "storecamp"),
    path("updatecamp/", updateCampPageView, name = "updatecamp"),
    path("updatehike/", updateHikePageView, name = "updatehike"),
]
