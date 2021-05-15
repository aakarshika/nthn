# Generated by Django 3.0.8 on 2020-08-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlittapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='p_created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='p_updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_photo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='qs_created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='qs_photo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='qs_ques_one',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='qs_ques_two',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='qs_updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='response',
            name='r_choice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='r_created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='response',
            name='r_updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='response',
            name='r_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v_photo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.Photo'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='settlittapp.User'),
        ),
    ]