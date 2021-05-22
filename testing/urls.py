from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('askquestion', views.ask_form, name='askquestion'),
    path('userdetail', views.user_form, name='userdetail'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    path('jobPosting',views.jobPosting,name='jobPosting'),
    path('tag/<str:id>/', views.tag, name='tag'),
    path('notes',views.notes,name='notes'),
    path('notes/<int:pk>',views.delete_notes,name='delete_notes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


























    # path('save-comment',views.save_comment,name='save-comment'),
