# Generated by Django 4.0.3 on 2022-03-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=64)),
                ('body', models.CharField(max_length=64)),
                ('head', models.CharField(max_length=64)),
                ('hands', models.CharField(max_length=64)),
                ('legs', models.CharField(max_length=64)),
            ],
        ),
    ]