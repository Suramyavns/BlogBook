from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='home'),
    path('loginUser',views.loginUser,name='Login'),
    path('registration',views.registerUser,name='registration'),
    path('logout',views.logoutUser,name='Logout'),
    path('profile/<int:id>',views.showprofile,name='profile'),
    path('update/<int:id>',views.updateprofile,name='update'),
    path('delete/<int:id>',views.deleteUser,name='deleteUser'),
    path('createBlog',views.createBlog,name='createBlog'),
    path('readBlog/<int:id>',views.readBlog,name='readBlog'),
    path('updateBlog/<int:id>',views.updateBlog,name='updateBlog'),
    path('deleteBlog/<int:id>',views.deleteBlog,name='deleteBlog'),
    path('blogAction/<int:id>/<int:preference>',views.blogAction,name='blogAction'),
    path('updateBlog,<int:id>',views.updateBlog,name='updateBlog'),
    path('createComment/<int:blogid>',views.createComment,name='createComment'),
    path('updateComment/<int:id>',views.updateComment,name='updateComment'),
    path('deleteComment/<int:id>',views.deleteComment,name='deleteComment'),
    path('commentAction/<int:id>/<int:preference>',views.commentAction,name='commentAction'),
    path('readReplies/<int:id>',views.readReplies,name="readReplies"),
    path('createReplies/<int:id>',views.createReply,name='createReply'),
    path('updateReply/<int:id>',views.updateReply,name='updateReply'),
    path('deleteReply/<int:id>',views.deleteReply,name='deleteReply'),
    path('replyAction/<int:id>/<int:preference>',views.replyAction,name='replyAction'),
    path('follow/<int:id>',views.follow,name='follow'),
    path('unfollow/<int:id>',views.unfollow,name='unfollow'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)