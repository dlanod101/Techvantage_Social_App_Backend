# Generated by Django 4.2.16 on 2024-09-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_category_project_contributors_project_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(default='general', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.CharField(default='general', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.CharField(default='general', max_length=255),
        ),
    ]
