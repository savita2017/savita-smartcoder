from django.urls import path
from .import views
from django.conf.urls import url

#Namespacing of app poll
app_name='polls'

urlpatterns=[
    url(r'^registeration/$',views.register,name='registeration'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
    path('activeuser_ques/',views.activeuser_ques,name='activeuser_ques'),
]