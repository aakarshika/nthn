from .models import User, Voter, Photo, Question, QuestionSet, Response
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'id',
            'u_username',
            'u_secret_id',
            'u_access_token',
            'u_joined_date'
            ]

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'id',
            'p_title', 
            'p_url_photo', 
            'p_about_pic'
            ]

class VoterSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='v_user', read_only=True)
    photo = PhotoSerializer(source='v_photo', read_only=True)
    
    class Meta:
        model = Voter
        fields = [
            'id',
            'v_about_me',
            'photo',
            'user'
            ]



class QuestionSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(source='q_photo', read_only=True)
    
    class Meta:
        model = Question
        fields = [
            'id', 
            'photo',
            'q_text' ,
            'q_code' ,
            'q_description' ,
            'q_total_votes' 
            ]


class QuestionSetSerializer(serializers.ModelSerializer):
    ques_one = QuestionSerializer(source='qs_ques_one', read_only=True)
    ques_two = QuestionSerializer(source='qs_ques_two', read_only=True)
    
    class Meta:
        model = QuestionSet
        fields = [
            'id', 
            'qs_photo' ,
            'qs_text' ,
            'ques_one' ,
            'ques_two' 
            ]


class ResponseSerializer(serializers.ModelSerializer):
    choice = QuestionSerializer(source='r_choice', read_only=True)
    user = UserSerializer(source='r_user', read_only=True)
    
    class Meta:
        model = Response
        fields = [
            'id', 
            'r_text_one' ,
            'r_text_two' ,
            'r_choice_code' ,
            'choice' ,
            'r_description' ,
            'r_response_milliseconds' ,
            'user' 
            ]






