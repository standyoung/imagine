# Generated by Django 4.2.11 on 2024-05-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_imageupload_image_imageupload_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='img_caption',
            field=models.TextField(blank=True, null=True, verbose_name='이미지 캡션'),
        ),
    ]
