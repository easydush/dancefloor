# Generated by Django 4.0.3 on 2022-03-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sex', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DanceSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('LOW', 'likes'), ('MEDIUM', 'is good in'), ('HIGH', 'is professional in')], max_length=10)),
                ('style', models.CharField(choices=[('RNB', 'RnB'), ('HIPHOP', 'hip-hop'), ('ELECTRODANCE', 'electrodance'), ('HOUSE', 'house'), ('POP', 'pop')], max_length=64)),
                ('dancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.dancer')),
            ],
        ),
    ]
