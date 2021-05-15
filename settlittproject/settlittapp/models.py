
from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class User(models.Model):
    u_username = models.CharField(max_length=35, null=True, default=None)
    u_secret_id = models.TextField(null=True, default=None)
    u_access_token = models.TextField(null=True, default=None)
    u_joined_date = models.DateTimeField('date joined', auto_now_add=True)
    u_created_date = models.DateTimeField('date created', auto_now_add=True)
    u_updated_date = models.DateTimeField('date updated', auto_now_add=True)
    
    def __str__(self):
       return ('' if (self.u_username == None)  else self.u_username )

    class Meta:
        ordering = ['u_joined_date']


class Photo(models.Model):
    p_title = models.CharField(max_length=35, null=True, default=None)
    p_about_pic = models.CharField(max_length=300, null=True, default=None)
    p_url_photo = models.CharField(max_length=5000, null=True, default=None)
    p_secret_id = models.TextField(null=True, default=None)
    p_uploaded_date = models.DateTimeField('date uploaded', auto_now_add=True)
    p_created_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    p_created_date = models.DateTimeField('date created', auto_now_add=True)
    p_updated_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    p_updated_date = models.DateTimeField('date updated', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.p_id, self.p_title)

class Voter(models.Model):
    # v_id = models.Field(primary_key=True)
    v_user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    v_about_me = models.CharField(max_length=300, null=True, default=None)
    v_photo = models.ForeignKey(Photo, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    v_secret_id = models.TextField(null=True, default=None)
    v_active = models.CharField(max_length=1000, null=True, default=None)
    v_created_date = models.DateTimeField('date created', auto_now_add=True)
    v_updated_date = models.DateTimeField('date updated', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.u_id, self.v_username)

class Question(models.Model):
    # q_id = models.Field(primary_key=True)
    q_photo = models.ForeignKey(Photo, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    q_text = models.CharField(max_length=200, null=True, default=None)
    q_code = models.CharField(max_length=200, null=True, default=None)
    q_description = models.TextField(null=True, default=None)
    q_total_votes = models.IntegerField()
    q_created_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    q_created_date = models.DateTimeField('date published', auto_now_add=True)
    q_updated_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    q_updated_date = models.DateTimeField('date published', auto_now_add=True)
    q_pub_date = models.DateTimeField('date published', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.q_text, self.q_code)


class QuestionSet(models.Model):
    # qs_id = models.Field(primary_key=True)
    qs_photo = models.ForeignKey(Photo, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    qs_text = models.CharField(max_length=200, null=True, default=None)
    qs_ques_one = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    qs_ques_two = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    qs_created_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    qs_created_date = models.DateTimeField('date published', auto_now_add=True)
    qs_updated_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    qs_updated_date = models.DateTimeField('date published', auto_now_add=True)
    qs_pub_date = models.DateTimeField('date published', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.qs_ques_one_id, self.qs_ques_two_id)


class Response(models.Model):
    # r_id = models.Field(primary_key=True)
    r_text_one = models.CharField(max_length=200, null=True, default=None)
    r_text_two = models.CharField(max_length=200, null=True, default=None)
    r_choice_code = models.CharField(max_length=200, null=True, default=None)
    r_choice = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    r_description = models.TextField(null=True, default=None)
    r_response_milliseconds = models.IntegerField()
    r_user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    r_created_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    r_created_date = models.DateTimeField('date created', auto_now_add=True)
    r_updated_by = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='+')
    r_updated_date = models.DateTimeField('date updated', auto_now_add=True)
    r_pub_date = models.DateTimeField('date published', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.r_id, self.r_choice_code)



