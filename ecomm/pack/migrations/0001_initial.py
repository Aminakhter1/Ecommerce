# Generated by Django 3.2.3 on 2022-05-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=800)),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='image/')),
            ],
        ),
    ]
