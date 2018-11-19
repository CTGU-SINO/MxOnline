__author__ = 'ct'
__date__ = '18-10-11 下午1:49'


from .views import (CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView)

from django.urls import path, re_path

# 要写上app的名字
app_name = "courses"

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    # path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comment"),
    # re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),
    re_path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name='video_play'),
]
