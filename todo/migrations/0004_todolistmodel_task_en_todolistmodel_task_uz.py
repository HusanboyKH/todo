# Generated by Django 4.2.3 on 2023-07-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todolistmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='task_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='todolistmodel',
            name='task_uz',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
