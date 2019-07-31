# Generated by Django 2.2.1 on 2019-05-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cartype', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]