from django.conf.urls import url
from first_app import views

# urlpatterns = [
#     url(r'^$',views.index,name='index'),
# ]

urlpatterns = [
    url(r'^$',views.first_app,name='index'),
]
