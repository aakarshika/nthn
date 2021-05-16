from django.db import models

# Create your models here.


class Response(models.Model):
    # r_id = models.Field(primary_key=True)
    r_text_one = models.CharField(max_length=200, null=True, default=None)
    r_text_two = models.CharField(max_length=200, null=True, default=None)
    r_choice_code = models.CharField(max_length=200, null=True, default=None)
    r_description = models.TextField(null=True, default=None)
    r_response_milliseconds = models.IntegerField()
    r_updated_date = models.DateTimeField('date updated', auto_now_add=True)
    r_pub_date = models.DateTimeField('date published', auto_now_add=True)
    # def __str__(self):
    #    return '{} {}'.format(self.r_id, self.r_choice_code)
