# Generated by Django 3.1.5 on 2021-01-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210108_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subhead',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]