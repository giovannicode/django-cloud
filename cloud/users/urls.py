from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'signup', views.UserCreateView.as_view(), name='signup'),
    url(r'signout', views.signout, name='signout'),
    url(r'signin', views.UserSigninView.as_view(), name='signin'),
)
