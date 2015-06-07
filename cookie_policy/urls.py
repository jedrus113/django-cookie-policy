from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^policy/?', views.policy_view, name='policy'),
    url(r'^accept-cookie-policy/?', views.acceptCookiePolicy_view, name='acceptCookiePolicy'),
]
