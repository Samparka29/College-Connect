from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobPosting(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    JOB_ID = models.CharField(max_length=100,default='')
    Company_Name = models.CharField(max_length=100,default='')
    Description=models.TextField(default='')
    Basic_Qualification=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Userdetail(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    username=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password= models.CharField(max_length=20)


# Question Model
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    tags=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Answer Model
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail


# UpVotes
class Upvote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')

# DownVotes
class Downvote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='downvote_user')


class Notes(models.Model):
    teacher=models.CharField( max_length=50)    
    subject=models.CharField( max_length=50) 
    pdf=models.FileField(upload_to='notes/pfds', max_length=100)

    def __str__(self):
        return self.teacher

    def delete(self,*args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)







# # Comment
# class Comment(models.Model):
#     answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
#     comment=models.TextField(default='')
#     add_time=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.comment            



