# Generated by Django 2.2.1 on 2019-05-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='returndate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='startdate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]