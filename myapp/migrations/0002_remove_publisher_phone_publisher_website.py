# Generated by Django 4.0.5 on 2022-06-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='phone',
        ),
        migrations.AddField(
            model_name='publisher',
            name='website',
            field=models.CharField(max_length=128, null=True),
        ),
    ]