from django.urls import path
from . import views

urlpatterns = [
    #URL에 이름을 붙인 것으로 뷰를 식별합니다. 뷰의 이름과 같을 수도 완전히 다를 수도 있습니다.
    #이름을 붙인 URL은 프로젝트의 후반에 사용할 거예요. 그러니 앱의 각 URL마다 이름 짓는 것은 중요합니다.
    #URL에 고유한 이름을 붙여, 외우고 부르기 쉽게 만들어야 해요.
    path('app_blog', views.app_blog, name='app_blog'),
    path('post_list', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('login', views.login, name="login"),
]