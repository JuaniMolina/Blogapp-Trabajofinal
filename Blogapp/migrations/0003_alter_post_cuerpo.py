# Generated by Django 4.1.3 on 2023-01-22 19:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0002_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
