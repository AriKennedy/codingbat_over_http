
from django.contrib import admin
from django.urls import path
from app.views import near_hundred, string_splosion, cat_dog, lone_sum
urlpatterns = [
    path('admin/', admin.site.urls),
    path('near-hundred/<int:n>', near_hundred),
    path('string-splosion/<str:s>', string_splosion),
    path('cat-dog/<str:s>', cat_dog),
    path('lone-sum/<int:a>/<int:b>/<int:c>', lone_sum),
]
