# Generated by Django 4.2.11 on 2024-06-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_img_imageupload_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='이미지'),
        ),
    ]
