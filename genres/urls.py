from django.urls import path
from genres.views import gender, gender_detail_view
urlpatterns = [
    path('', view=gender, name="genres_list"),
    path('<int:pk>', gender_detail_view, name="gender_detail_view"),
]