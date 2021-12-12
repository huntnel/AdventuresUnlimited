from django.urls import path
from .views import indexPageView, storeHikePageView, updateCampPageView, updateHikePageView, campingPageView
from .views import hikingPageView, createHikePageView, createCampPageView, updateHikePageView, updateCampPageView
<<<<<<< HEAD
from .views import deleteCampPageView, deleteHikePageView, editCampPageView, aboutPageView, storeCampPageView

=======
from .views import deleteCampPageView, deleteHikePageView, aboutPageView, editCampPageView
>>>>>>> 008fb1e821c8efa9fd1532058cda7606037cafb0

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about/", aboutPageView, name="about"),
    path("camping/", campingPageView, name = "camping"),
    path("createcamp/", createCampPageView, name = "createcamp"),
    path("storecamp/", storeCampPageView, name = "storecamp"),
    path("editcamp/<int:campid>/", editCampPageView, name = "editcamp"),
    path("updatecamp/<int:id>/", updateCampPageView, name = "updatecamp"),
    path("deletecamp/<int:id>/", deleteCampPageView, name = "deletecamp"),
    path("hiking/", hikingPageView, name = "hiking"),
    path("createhike/", createHikePageView, name = "createhike"),
    path("edithike/", updateHikePageView, name = "updatehike"),
    path("updatehike/", updateHikePageView, name = "updatehike"),
    path("deletehike/", deleteHikePageView, name = "deletehike"),
]
