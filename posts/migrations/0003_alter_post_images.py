# Generated by Django 3.2 on 2022-07-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220707_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(null=True, upload_to='D:\\Users\\Code\\Projects\\BSP Recruitment\\BSPForum\\uploaded_files'),
        ),
    ]
