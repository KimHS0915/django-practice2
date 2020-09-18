# Generated by Django 3.0.10 on 2020-09-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200918_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='48px * 48px 크기의 png/jpg 파일을 업로드해주세요.', upload_to='accounts/avatar/%Y/%m/%d'),
        ),
    ]
