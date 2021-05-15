# Generated by Django 3.0.8 on 2020-08-03 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(default=None, max_length=35, null=True)),
                ('p_about_pic', models.CharField(default=None, max_length=300, null=True)),
                ('p_url_photo', models.CharField(default=None, max_length=5000, null=True)),
                ('p_secret_id', models.TextField(default=None, null=True)),
                ('p_uploaded_date', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('p_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('p_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_text', models.CharField(default=None, max_length=200, null=True)),
                ('q_code', models.CharField(default=None, max_length=200, null=True)),
                ('q_description', models.TextField(default=None, null=True)),
                ('q_total_votes', models.IntegerField()),
                ('q_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('q_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('q_pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(default=None, max_length=35, null=True)),
                ('u_secret_id', models.TextField(default=None, null=True)),
                ('u_access_token', models.TextField(default=None, null=True)),
                ('u_joined_date', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('u_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('u_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
            ],
            options={
                'ordering': ['u_joined_date'],
            },
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_about_me', models.CharField(default=None, max_length=300, null=True)),
                ('v_secret_id', models.TextField(default=None, null=True)),
                ('v_active', models.CharField(default=None, max_length=1000, null=True)),
                ('v_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('v_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
                ('v_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo')),
                ('v_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_text_one', models.CharField(default=None, max_length=200, null=True)),
                ('r_text_two', models.CharField(default=None, max_length=200, null=True)),
                ('r_choice_code', models.CharField(default=None, max_length=200, null=True)),
                ('r_description', models.TextField(default=None, null=True)),
                ('r_response_milliseconds', models.IntegerField()),
                ('r_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('r_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date updated')),
                ('r_pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('r_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question')),
                ('r_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
                ('r_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
                ('r_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qs_text', models.CharField(default=None, max_length=200, null=True)),
                ('qs_created_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('qs_updated_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('qs_pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('qs_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
                ('qs_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo')),
                ('qs_ques_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question')),
                ('qs_ques_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question')),
                ('qs_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='q_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='q_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo'),
        ),
        migrations.AddField(
            model_name='question',
            name='q_updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AddField(
            model_name='photo',
            name='p_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AddField(
            model_name='photo',
            name='p_updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
    ]
