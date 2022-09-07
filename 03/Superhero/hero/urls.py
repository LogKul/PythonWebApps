from django.urls import path
from .views import MobView, WayneView, IndexView, SuperMonkeyView

urlpatterns = [
    path('', IndexView.as_view()),
    path('mob', MobView.as_view()),
    path('wayne', WayneView.as_view()),
    path('supermonkey', SuperMonkeyView.as_view()),
]
