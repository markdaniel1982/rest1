# Generated by Django 3.2.19 on 2023-06-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_mianao', upload_to='images/'),
        ),
    ]
