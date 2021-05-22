from django.contrib import admin
from . models import *


# Register your models here.
class JobPostingAdmin(admin.ModelAdmin):
    list_display=('title','JOB_ID','Description','Basic_Qualification','Company_Name')
admin.site.register(JobPosting,JobPostingAdmin)   

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')
    search_fields=('title','detail')
admin.site.register(Question,QuestionAdmin) 
admin.site.register(Answer) 


class UpvoteAdmin(admin.ModelAdmin):
    list_display=('answer','user')
admin.site.register(Upvote,UpvoteAdmin)

class DownvoteAdmin(admin.ModelAdmin):
    list_display=('answer','user')
admin.site.register(Downvote,DownvoteAdmin) 







# class CommentAdmin(admin.ModelAdmin):
#     list_display=('answer','comment')
# admin.site.register(Comment,CommentAdmin)
 