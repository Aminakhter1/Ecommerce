# Generated by Django 3.2.3 on 2022-05-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advatisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.FileField(default=None, max_length=250, null=True, upload_to='image/')),
                ('image_2', models.FileField(default=None, max_length=250, null=True, upload_to='image/')),
                ('image_3', models.FileField(default=None, max_length=250, null=True, upload_to='image/')),
            ],
        ),
    ]
