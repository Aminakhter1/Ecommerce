# Generated by Django 3.2.3 on 2022-06-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0006_auto_20220608_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='advatisment',
            name='image_sandle_1',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='advatisment',
            name='image_sleeper_1',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='image/'),
        ),
    ]
