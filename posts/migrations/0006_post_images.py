# Generated by Django 3.2 on 2022-07-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='D:\\Users\\Code\\Projects\\BSP Recruitment\\BSPForum\\uploaded_files'),
        ),
    ]
